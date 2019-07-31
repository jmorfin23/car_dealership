from app import app, db
from datetime import datetime

#don't need just from the tutorial
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

#for the table 'account' in the database
class Account(db.Model):
    account_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    address_id = db.Column(db.Integer)
    phone = db.Column(db.Integer)
    date_created = db.Column(db.DateTime, default=datetime.now().date())
