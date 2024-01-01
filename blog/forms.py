from flask_wtf import FlaskForm
from sqlalchemy import select
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError
from wtforms.validators import InputRequired, Length, Email, EqualTo
from blog.models import User
from blog import db

class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired(), Length(min=2, max=10)])
    email = StringField("Email", validators=[InputRequired(), Email()])
    password = PasswordField("Password", validators=[InputRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[InputRequired(), EqualTo("password")])
    submit = SubmitField("Sign Up")

    def validate_username(self, field):
        queried_username = db.session.execute(select(User.username).filter_by(username=field.data)).first()
        if queried_username:
            raise ValidationError("Try using another username. This username is already taken")
        return True
    
    def validate_email(self, field):
        queried_email = db.session.execute(select(User.email).filter_by(email=field.data)).first()
        if queried_email:
            raise ValidationError("Try using another email. This email is already taken")
        return True
        

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[InputRequired(), Email()])
    password = PasswordField("Password", validators=[InputRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Login")
