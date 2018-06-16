from notes_app import *

class User(db.Model):
	__tablename__ = "users"
	u_id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True, nullable=False)
	password = db.Column(db.String(77))
	email = db.Column(db.String(80), nullable=False)
	rating = db.Column(db.Integer, default=conf_d['user_def_rating'])

class Page(db.Model):
	__tablename__ = "pages"
	p_id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(80), unique=True, nullable=False)
	url = db.Column(db.String(800), nullable=False)
	rating = db.Column(db.Integer, default=conf_d['page_def_rating'], nullable=False)

class Votes(db.Model):
	__tablename__ = "votes"
	v_id = db.Column(db.Integer, primary_key=True)
	u_id = db.Column(db.Integer, nullable=False)
	p_id = db.Column(db.Integer, nullable=False)
	updown = db.Column(db.Boolean, nullable=False)

db.create_all()