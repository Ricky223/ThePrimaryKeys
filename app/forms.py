from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, HiddenField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
import csi3335sp2022
from app.models import User, teamsTable
from flask_login import current_user, login_user
from flask import session

import pymysql


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


def createEnterTeamYearForm(viewTeamName, viewUsername):
    class EnterTeamYear(FlaskForm):
        usernameHidden = HiddenField('username')
        con = pymysql.connect(host=csi3335sp2022.mysql["location"], user=csi3335sp2022.mysql["user"],
                              password=csi3335sp2022.mysql["password"],
                              database=csi3335sp2022.mysql["db"])

        data = []
        with con:
            cur = con.cursor()
            currUser = User.query.filter_by(username = viewUsername).first()
            team = teamsTable.query.filter_by(user_id = currUser.id).order_by(teamsTable.timestamp.desc()).first()
            sql = """select distinct yearID from team where name = %s"""
            cur.execute(sql, team.team_choose)
            results = cur.fetchall()
            for row in results:
                data.append(row[0])

        Years = ["1999", "2000", "2001", "2002", "2003"]
        year = SelectField('Year:', choices=data)
        submit = SubmitField('Submit')
    return EnterTeamYear
