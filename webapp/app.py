from email.mime import image
from flask import Flask, current_app, render_template, send_file, send_from_directory, url_for, flash, jsonify, request
from forms import InputForm
import requests, secrets, ast, os
import shutil

app = Flask(__name__)
app.config['SECRET_KEY'] = '36d2fcd2731047780f1b3f9025e1b59f'

def rm_files(folder):
    for filename in os.listdir(folder):
        os.remove(os.path.join(folder, filename))

@app.route('/downloadRestoredImage/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    return send_file(filename,as_attachment=True)

@app.route('/aboutUs', methods=['GET'])
def aboutUs():
    return render_template('aboutUs.html')

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')



def save_image(image_data):
     random_hex = secrets.token_hex(8)
     _, f_ext = os.path.splitext(image_data.filename)
     picture_fn = random_hex + f_ext
     picture_path = os.path.join(app.root_path, 'static/images', picture_fn)
     image_data.save(picture_path)
     return picture_fn

def restorer(image_file):
    # Command
    restored_image=""
    return restored_image


@app.route("/home", methods=['POST', 'GET'])
def input_pic():
    
    form  = InputForm()
   
    if form.validate_on_submit():
        
        flash('Validated successfully', 'success')
        rm_files('static/images')
        rm_files('static/imgs')
        
        image_fn = save_image(form.picture.data)
        image_file = url_for('static', filename = 'images/' + image_fn)
        print(image_file)

        restored_image=restorer(image_file)
        #return render_template('restore.html',orignal_image=image_file,restored_image=restored_image)

        return render_template('restore.html',orignal_image=image_file,restored_image=image_file)
    return render_template('home.html', form=form)



if __name__ == '__main__':
    app.run(debug=True)



