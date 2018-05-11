import os
from flask import Flask, request, send_from_directory, render_template, url_for, send_file, url_for, redirect, jsonify
from werkzeug.utils import secure_filename
UPLOAD_FOLDER = 'uploads/'
app = Flask(__name__, static_folder='', static_url_path='')

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def redhome():
    return redirect(url_for('index'))

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/about.html')
def home():
    return render_template('about.html')


@app.route('/upload.html')
def upload():
    return render_template('upload.html')


@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/translate.html')
def translate():
#    imagefile = request.files.get('fileToUpload')
#    print(imagefile)
#    filename = secure_filename(imagefile.filename)
#    imagefile.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#    return send_from_directory(app.config['UPLOAD_FOLDER'], imagefile.filename)
    return render_template('translate.html')

#@app.route('/uploadimg', methods = ['POST'])
#def uploadimg():
#    print("1")
#    imagefile = request.files.get('image')
#    print("1")
#    print(imagefile)
#    print("1")
#    filename = secure_filename("1.jpg")
#    print("1")
#    imagefile.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#    print("1")
#    return jsonify({"success": True})

@app.route('/uploadimg', methods = ['POST'])
def uploadimg():
    imagefile = request.files.get('fileToUpload')
    print(imagefile)
    filename = secure_filename("1.jpg")
    imagefile.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return send_from_directory(app.config['UPLOAD_FOLDER'], imagefile.filename)

@app.route('/<path:path>')
def send_js(path):
    return send_from_directory('', path)




if __name__ == '__main__':
    app.run(debug=True)