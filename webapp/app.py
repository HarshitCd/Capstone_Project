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
        
        return render_template('home.html', title='Username', form=form, image_file=image_file)
    return render_template('home.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)