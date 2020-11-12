from . import db

class Admin(db.Model):
    __tablename__ = "admin"
    admin_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.BLOB)
    salt = db.Column(db.BLOB)

class User(db.Model):
    __tablename__ = "user"
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.BLOB)
    salt = db.Column(db.BLOB)

class Team(db.Model):
    __tablename__ = "team"
    team_id = db.Column(db.Integer, primary_key=True)
    teamname = db.Column(db.String)

class UserTeam(db.Model):
    __tablename__ = "userteam"
    userteam_id = db.Column(db.Integer, primary_key=True)
    team_id =  db.Column(db.Integer, db.ForeignKey("team.team_id"))
    user_id =  db.Column(db.Integer, db.ForeignKey("user.user_id"))

class Submission(db.Model):
    __tabelname__ = "submission"
    submission_id = db.Column(db.Integer, primary_key=True)
    team_id =  db.Column(db.Integer, db.ForeignKey("team.team_id"))
    user_id =  db.Column(db.Integer, db.ForeignKey("user.user_id"))
    upload_time = db.Column(db.DateTime)
    score = db.Column(db.Integer)
    tag = db.Column(db.String)


