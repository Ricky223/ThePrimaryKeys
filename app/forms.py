from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
import csi3335sp2022
from app.models import User, teamsTable
from sqlalchemy.sql import select
import pymysql


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')


class EnterTeamName(FlaskForm):
    con = pymysql.connect(host=csi3335sp2022.mysql["location"], user=csi3335sp2022.mysql["user"],
                          password=csi3335sp2022.mysql["password"],
                          database=csi3335sp2022.mysql["db"])
    data = []
    with con:
        cur = con.cursor()
        sql = """select distinct name from team"""
        cur.execute(sql)
        results = cur.fetchall()
        for row in results:
            data.append(row[0])

    team = SelectField('Team Name:', choices=data)
    submit = SubmitField('Submit')


class EnterTeamYear(FlaskForm):

    con = pymysql.connect(host=csi3335sp2022.mysql["location"], user=csi3335sp2022.mysql["user"],
                          password=csi3335sp2022.mysql["password"],
                          database=csi3335sp2022.mysql["db"])

    data = []
    with con:
        cur = con.cursor()

        sql = """select distinct yearID from team where name = %s"""
        s = select(teamsTable)
        # for val in s:
        #     teamRead = val[1]
        cur.execute(sql, s)
        results = cur.fetchall()
        for row in results:
            data.append(row[0])

    Years = ["1999", "2000", "2001", "2002", "2003"]
    year = SelectField('Year', choices=Years)
    submit = SubmitField('Submit')


