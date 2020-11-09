from . import db

class Admin(db.Model):
    __tablename__ = "admin"
    admin_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.BLOB)
    salt = db.Column(db.BLOB)
