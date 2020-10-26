import os
from pathlib import Path
import urllib.request
from flask import Flask, flash, request, redirect, render_template_string
from werkzeug.utils import secure_filename
import boto3

INSTANCE_HOSTNAME = urllib.request.urlopen('http://169.254.169.254/latest/meta-data/public-hostname').read().decode()

UPLOAD_FOLDER = '/tmp/uploads'
Path(UPLOAD_FOLDER).mkdir(parents=True, exist_ok=True)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = 'DEMO-APP'
FILE_UPLOAD_BUCKET_NAME = os.environ['FILE_UPLOAD_BUCKET_NAME']


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)

        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        s3_client = boto3.client('s3')
        s3_client.upload_file(file_path, FILE_UPLOAD_BUCKET_NAME, filename)

        os.remove(file_path)

        return redirect('/')

    s3 = boto3.resource('s3')
    bucket_obj = s3.Bucket(FILE_UPLOAD_BUCKET_NAME)
    uploaded_files = bucket_obj.objects.all()

    return render_template_string('''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File - {{ instance_hostname }}</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    <h2>Uploaded Files</h2>
    {% for file_object in uploaded_files %}
      <p>{{ file_object.key }}</p>
    {% endfor %}
    ''', uploaded_files=uploaded_files, instance_hostname=INSTANCE_HOSTNAME)


app.run(host='0.0.0.0')
