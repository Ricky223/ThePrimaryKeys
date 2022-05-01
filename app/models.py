from datetime import datetime
from app import db, login, admin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, current_user
from flask_admin.contrib.sqla import ModelView



class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    teams = db.relationship('teamsTable', backref='usert', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class teamsTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team_choose = db.Column(db.String(256))
    year_choose = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Team {}>'.format(self.team_choose,self.year_choose)


class adminView(ModelView):
    def is_accessible(self):
        return current_user.username == "Admin"


admin.add_view(adminView(User, db.session))
admin.add_view(adminView(teamsTable, db.session))

@login.user_loader
def load_user(id):
    return User.query.get(int(id))