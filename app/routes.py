import csi3335sp2022
from app import app
from flask import render_template, flash, redirect, url_for, request, session
from app.forms import LoginForm, EnterTeamName, EnterTeamYear
from flask_login import current_user, login_user
from app.models import User, teamsTable
from flask_login import logout_user, login_required
from werkzeug.urls import url_parse
from app import db
from app.forms import RegistrationForm
from app.player import Player
import pymysql


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        # TODO: index waited to implement
        return redirect(url_for('enter'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('enter')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


# TODO: not sure if needed
@app.route('/base')
def base():
    return render_template('base.html', title="Base")


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


# TODO: index waited to be implement
@app.route('/')
@app.route('/enter', methods=['GET', 'POST'])
@login_required
def enter():
    form = EnterTeamName()
    if form.validate_on_submit():
        print(form.team.data, flush=True)
        session['teamName'] = form.team.data
        tableDB = teamsTable(team_choose=form.team.data, user_id=current_user)
        db.session.add(tableDB)
        # TODO: Not Working
        db.session.commit()
        return redirect(url_for('enterYear'))
    return render_template('enterTeamName.html', form=form)


@app.route('/')
@app.route('/enteryear', methods=['GET', 'POST'])
@login_required
def enterYear():
    form = EnterTeamYear()
    team = session.get('teamName', None)
    if form.validate_on_submit():
        print(form.year.data, flush=True)
        session['year'] = form.year.data
        return redirect(url_for('table'))
    return render_template('enterTeamYear.html', form=form, team=team)


@app.route('/tableplayer')
@login_required
def table():
    con = pymysql.connect(host=csi3335sp2022.mysql["location"], user=csi3335sp2022.mysql["user"], password=csi3335sp2022.mysql["password"],
                          database=csi3335sp2022.mysql["db"])
    data = []
    with con:
        cur = con.cursor()
        sql1 = """select distinct teamID from team where name = %s"""
        cur.execute(sql1,session.get('teamName', None))
        teamID = cur.fetchone()
        sql = """select concat(p.nameFirst, ' ', p.nameLast) , a.Gs from appearances a natural join people p where a.teamID = %s and yearID = %s;"""
        tuple1 = (teamID, session.get('year', None))
        cur.execute(sql,tuple1)
        results = cur.fetchall()

        for row in results:
            data.append(Player(row[0],row[1]))



    values = [Player('Ricky', 12), Player('Varun', 13)]
    team = session.get('teamName', None)
    year = session.get('year', None)
    return render_template('playerTable.html', values=data, team=team, year=year)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('enter'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
