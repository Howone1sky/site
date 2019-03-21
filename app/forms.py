from flask_wtf import Form
from wtforms import StringField, BooleanField, PasswordField
from wtforms.validators import DataRequired


class LoginForm(Form):
    login = StringField('login', validators=[DataRequired()])
    password = PasswordField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=True)
    men = BooleanField('men', default=False)
    women = BooleanField('women', default=False)
