from flask import session
from flask.ext.sqlalchemy import SQLAlchemy
import hashlib
import mailchimp
from Feather import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/data.db'
db = SQLAlchemy(app)


#: Define the Section class
class Section(db.Model):
	name = db.Column(db.String(20), primary_key=True)
	title = db.Column(db.String(75))
	content = db.Column(db.Text)

	def __init__(self, name, title, content):
		self.title = title
		self.name = name
		self.content = content

	def __repr__(self):
		return '<Section %r (%d)>' % self.name, self.id

	@classmethod
	def get_all(cls):
		return cls.query.all()

	@classmethod
	def get_content(cls, name):
		return cls.query.filter_by(name=name).first().content

	@classmethod
	def get_args(cls):
		args = {}
		for section in Section.get_all():
			args[section.name] = section.content
		return args

	@classmethod
	def get(cls, name):
		return cls.query.filter_by(name=name).first()


class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(30), unique=True)
	password = db.Column(db.String(75))

	def __init__(self, username, password):
		self.username = username
		self.password = hashlib.sha224(password).hexdigest()

	def __repr__(self):
		return '<User %r>' % self.username

	@staticmethod
	def is_logged_in():
		try:
			session['user']
		except:
			return False
		return session['user']

	@staticmethod
	def hash_password(password):
		return hashlib.sha224(password).hexdigest()

	@classmethod
	def get(cls, username):
		return cls.query.filter_by(username=username).first()


class SystemProperty(db.Model):
	attr = db.Column(db.String(20), primary_key=True)
	value = db.Column(db.String(75))
	custom = db.Column(db.Boolean, default=False)

	def __init__(self, attr, value, custom):
		self.attr = attr
		self.value = value
		self.custom = custom

	def __repr__(self):
		return '<System Property %r>' % self.attr

	@classmethod
	def get(cls, attr):
		return cls.query.filter_by(attr=attr).first().value

	@classmethod
	def get_custom_properties(cls):
		return cls.query.filter_by(custom=True)

	@classmethod
	def get_full(cls, attr):
		return cls.query.filter_by(attr=attr).first()


#: Define the mailchimp class
class MC(object):
	def __init__(self, api_key, list_id):
		try:
			self.api = mailchimp.Mailchimp(api_key)
		except:
			self.api = False
		self.list_id = list_id

	def subscribe_user(self, email, merge_vars={}):
		if not self.api:
                        self.api.lists.subscribe(self.list_id, email, merge_vars)