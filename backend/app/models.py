from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

class Part(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    customer = db.relationship('Customer', backref=db.backref('parts', lazy=True))

class Revision(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    part_id = db.Column(db.Integer, db.ForeignKey('part.id'), nullable=False)
    part = db.relationship('Part', backref=db.backref('revisions', lazy=True))

class Trial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    part_id = db.Column(db.Integer, db.ForeignKey('part.id'), nullable=False)
    part = db.relationship('Part', backref=db.backref('trials', lazy=True))

class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    trial_id = db.Column(db.Integer, db.ForeignKey('trial.id'), nullable=True)
    trial = db.relationship('Trial', backref=db.backref('files', lazy=True))
