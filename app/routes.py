from app import app
from flask import render_template, flash, redirect, url_for, request
from app.forms import LoginForm
from flask_login import current_user, login_user
from app.models import User
from flask_login import logout_user, login_required
from werkzeug.urls import url_parse
from app import db
from app.forms import RegistrationForm


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
@app.route('/enter')
@login_required
def enter():
    Pokemons = ["Pikachu", "Charizard", "Squirtle", "Jigglypuff",
                "Bulbasaur", "Gengar", "Charmander", "Mew", "Lugia", "Gyarados"]
    return render_template('enterTeamName.html', team=Pokemons)


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