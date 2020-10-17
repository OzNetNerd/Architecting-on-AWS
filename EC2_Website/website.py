import os
from pathlib import Path
from flask import Flask, flash, request, redirect, render_template_string
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/tmp/uploads'
Path(UPLOAD_FOLDER).mkdir(parents=True, exist_ok=True)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = 'DEMO-APP'


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
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect('/')

    uploaded_files = os.listdir(UPLOAD_FOLDER)

    return render_template_string('''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    <h2>Uploaded Files</h2>
    {% for filename in uploaded_files %}
      <p>{{ filename }}</p>
    {% endfor %}
    ''', uploaded_files=uploaded_files)


app.run(host='0.0.0.0')
