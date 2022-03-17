from flask import Flask, render_template, url_for, flash
from forms import InputForm
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '36d2fcd2731047780f1b3f9025e1b59f'

@app.route("/", methods=['POST', 'GET'])
@app.route("/home", methods=['POST', 'GET'])
def input_pic():
    form  = InputForm()
    if form.validate_on_submit():
        flash(f'Validated successfully\nUsername: {form.username.data}', 'success')
        data = {
            "data": form.username.data
        }
        data = requests.post("http://127.0.0.1:5000/", data=data).text
        return render_template('home.html', title='Username', form=form, username=data)
    return render_template('home.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)