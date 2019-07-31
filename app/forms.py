from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class FindForm(FlaskForm):
    name = StringField('Enter Name', validators=[DataRequired()])
    submit = SubmitField('Submit')
