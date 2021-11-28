from database_init import db
from datetime import date, datetime

class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(256))
    views = db.Column(db.Integer, default=0)
    shorten_url = db.Column(db.Integer, unique=True)
    date_created = db.Column(db.DateTime, default=datetime.now())

    