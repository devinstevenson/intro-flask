from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class MessageForm(Form):
    title = StringField('Title', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired(), Length(max=140)])
