from datetime import datetime as dt
from app import db
from flask import current_app


class URL(db.Model):
    id        = db.Column(db.Integer, primary_key=True)
    ip        = db.Column(db.String(35), nullable=False)
    url       = db.Column(db.Text, nullable=False)
    url_short = db.Column(db.String(30), nullable=False, unique=True)
    count     = db.Column(db.Integer, nullable=False, default=0)
    ips       = db.relationship('ips', backref='ips', lazy=True)

    def __repr__(self):
        return f'<URL: {self.ip}, {self.url}, {self.url_short}, {self.count}>'

class ips(db.Model):
    id    = db.Column(db.Integer, primary_key=True)
    urlID = db.Column(db.Integer, db.ForeignKey('url.id'), nullable=False)
    ip    = db.Column(db.String(35), nullable=False)
    info  = db.Column(db.Text, nullable=False)
