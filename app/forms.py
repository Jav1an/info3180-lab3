from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Email, length, Regexp

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), length(max=150), Regexp(r'^[A-Za-z\s\-]+$', message="Name must contain only letters")])
    email = StringField('E-mail', validators=[DataRequired(), Email(), length(max=150)])
    subject = StringField('Subject', validators=[DataRequired(), length(max=200)])
    message = TextAreaField('Message', validators=[DataRequired()])