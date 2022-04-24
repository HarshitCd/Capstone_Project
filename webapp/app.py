from email.mime import image
from flask import Flask, render_template, url_for, flash, jsonify
from forms import InputForm
import requests, secrets, ast, os
import shutil

app = Flask(__name__)
app.config['SECRET_KEY'] = '36d2fcd2731047780f1b3f9025e1b59f'

def rm_files(folder):
    for filename in os.listdir(folder):
        os.remove(os.path.join(folder, filename))


def save_image(image_data):
     random_hex = secrets.token_hex(8)
     _, f_ext = os.path.splitext(image_data.filename)
     picture_fn = random_hex + f_ext
     picture_path = os.path.join(app.root_path, 'static/images', picture_fn)
     image_data.save(picture_path)
     return picture_fn

def restorer(image_file):
    restored_image=""
    return restored_image

@app.route("/", methods=['POST', 'GET'])
@app.route("/home", methods=['POST', 'GET'])
def input_pic():
    
    form  = InputForm()
    if form.validate_on_submit():
        
        flash('Validated successfully', 'success')
        rm_files('static/images')
        
        image_fn = save_image(form.picture.data)
        image_file = url_for('static', filename = 'images/' + image_fn)
        print(image_file)

        restored_image=restorer(image_file)
        #return render_template('restore.html',orignal_image=image_file,restored_image=restored_image)

        return render_template('restore.html',orignal_image=image_file,restored_image=image_file)
    return render_template('home.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)


# #app.py
# from flask import Flask, flash, request, redirect, url_for, render_template
# import urllib.request
# import os
# from werkzeug.utils import secure_filename
# import requests, secrets, ast, os
# import shutil
 
# app = Flask(__name__)
 
# UPLOAD_FOLDER = 'static/images/'
 
# app.secret_key = "secret key"
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
 
# ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
 
# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
     
 
# @app.route('/')
# def home():
#     return render_template('index.html')
 
# @app.route('/', methods=['POST'])
# def upload_image():
#     if 'file' not in request.files:
#         flash('No file part')
#         return redirect(request.url)
#     file = request.files['file']
#     if file.filename == '':
#         flash('No image selected for uploading')
#         return redirect(request.url)
#     if file and allowed_file(file.filename):
#         filename = secure_filename(file.filename)
#         file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#         #print('upload_image filename: ' + filename)
#         flash('Image successfully uploaded and displayed below')
#         return render_template('index.html', filename=filename)
#     else:
#         flash('Allowed image types are - png, jpg, jpeg, gif')
#         return redirect(request.url)
 
# @app.route('/display/<filename>')
# def display_image(filename):
#     #print('display_image filename: ' + filename)
#     return redirect(url_for('static', filename='images/' + filename), code=301)
 
# if __name__ == "__main__":
#     app.run()

