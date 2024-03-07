from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired


class DepartForm(FlaskForm):
    title_of_department = StringField('Title of department', validators=[DataRequired()])
    chief = StringField('Босс', validators=[DataRequired()])
    members = StringField('участники', validators=[DataRequired()])
    department_email = StringField('почта департамента', validators=[DataRequired()])
    submit = SubmitField('Применить')