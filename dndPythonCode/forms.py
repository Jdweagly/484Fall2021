from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class InputForm(FlaskForm):
    character_name = StringField('Character Name', validators=[DataRequired()])
    submit = SubmitField('Submit')
