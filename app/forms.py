from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectMultipleField, SelectField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User



class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    # TODO: email validators
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    # TODO: Not sure if really need this
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')


class EnterTeamName(FlaskForm):
    Pokemons = ["Pikachu", "Charizard", "Squirtle", "Jigglypuff",
                "Bulbasaur", "Gengar", "Charmander", "Mew", "Lugia", "Gyarados"]

    team = SelectField('Team Name:', choices=Pokemons)
    submit = SubmitField('Submit')


class EnterTeamYear(FlaskForm):
    Years = ["1999", "2000", "2001", "2002", "2003"]
    year = SelectField('Year', choices=Years)
    sumbit = SubmitField('Submit')