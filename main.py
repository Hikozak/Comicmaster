import os
from flask import Flask, request, send_from_directory, render_template, url_for, send_file
from werkzeug.utils import secure_filename
UPLOAD_FOLDER = 'C:\\Users\\Mango Float\\Documents\\GitHub\\Comicmaster\\uploads'
app = Flask(__name__, static_folder='', static_url_path='')

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/about.html')
def home():
    return render_template('about.html')


@app.route('/upload.html')
def upload():
    return render_template('upload.html')


@app.route('/translate.html')
def translate():
#    imagefile = request.files.get('fileToUpload')
#    print(imagefile)
#    filename = secure_filename(imagefile.filename)
#    imagefile.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#    return send_from_directory(app.config['UPLOAD_FOLDER'], imagefile.filename)
    return render_template('translate.html')

@app.route('/<path:path>')
def send_js(path):
    return send_from_directory('', path)




if __name__ == '__main__':
    app.run(debug=True)