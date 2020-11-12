from . import db

class User(db.Model):
    __tablename__ = "user"
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    team_name = db.Column(db.String)
    password = db.Column(db.BLOB)
    salt = db.Column(db.BLOB)

class Submission(db.Model):
    __tablename__ = "submission"
    submission_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"))
    upload_time = db.Column(db.DateTime)
    tag = db.Column(db.String)
    score = db.Column(db.Integer)
