from wsgiref.validate import validator
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class InputForm(FlaskForm):
    picture = FileField('Upload Image', validators=[DataRequired(), FileAllowed(['png', 'jpg', 'jpeg', 'gif'])])
    submit = SubmitField('Restore Image')