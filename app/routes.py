import csi3335sp2022
from app import app
from flask import render_template, flash, redirect, url_for, request, session
from app.forms import LoginForm, EnterTeamName, createEnterTeamYearForm
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
        currUser = User.query.filter_by(username=current_user.username).first()
        team = teamsTable(team_choose=form.team.data, user_id=currUser.id)
        db.session.add(team)
        db.session.commit()
        session['teamName'] = form.team.data
        return redirect(url_for('enterYear'))
    return render_template('enterTeamName.html', form=form)


@app.route('/')
@app.route('/enteryear', methods=['GET', 'POST'])
@login_required
def enterYear():
    # hello
    creator = createEnterTeamYearForm(session['teamName'], current_user.username)
    form = creator()
    form.usernameHidden = current_user.username
    team = session.get('teamName', None)
    if form.validate_on_submit():
        print(form.year.data, flush=True)
        currUser = User.query.filter_by(username=current_user.username).first()
        teamToUpdate = teamsTable.query.filter_by(user_id=currUser.id).order_by(teamsTable.timestamp.desc()).first()
        teamToUpdate.year_choose = form.year.data
        db.session.commit()
        session['year'] = form.year.data
        return redirect(url_for('table'))
    return render_template('enterTeamYear.html', form=form, team=team)


@app.route('/tableplayer')
@login_required
def table():
    con = pymysql.connect(host=csi3335sp2022.mysql["location"], user=csi3335sp2022.mysql["user"],
                          password=csi3335sp2022.mysql["password"],
                          database=csi3335sp2022.mysql["db"])
    data = []
    with con:
        cur = con.cursor()
        sql1 = """select distinct teamID from team where name = %s"""
        cur.execute(sql1, session.get('teamName', None))
        teamID = cur.fetchone()

        # sql = """select concat(p.nameFirst, ' ', p.nameLast) , a.Gs from appearances a natural join people p where a.teamID = %s and yearID = %s;"""
        sqlgetIDs = """select distinct playerID from appearances where teamID = %s and yearID = %s"""
        tupleIDs = (teamID, session['year'])
        cur.execute(sqlgetIDs, tupleIDs)
        resultIDs = cur.fetchall()

        sqlGetPlayTime = """select G_p, G_c, G_1b, G_2b, G_3b, G_ss, G_lf, G_cf, G_of, G_dh, G_ph, G_pr from appearances where teamID = %s and yearID = %s and playerID = %s"""
        sqlgetPlayerName = """select concat(nameFirst, ' ', nameLast) from people where playerID = %s"""
        for row in resultIDs:
            cur.execute(sqlgetPlayerName, row)
            pID = cur.fetchone()
            tuplePlayTime = (teamID, session['year'], row)
            cur.execute(sqlGetPlayTime, tuplePlayTime)
            playTimeResults = cur.fetchall()
            for row1 in playTimeResults:
                data.append(Player(pID, row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11]))

    positions = ['Pitcher', 'Catcher', 'First Base Man', 'Second Base Man', 'Third Base Man', 'Short Stop',
                 'Left Fielder'
                 'Center Fielder', 'Right Fielder', 'OutFielder', 'Designated Hitter', 'Pinch Hitter', 'Pinch Runner']
    team = session.get('teamName', None)
    year = session.get('year', None)
    return render_template('playerTable.html', values=data, team=team, year=year, positions=positions)


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
