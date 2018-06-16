import os, sys
import yaml

from flask import *
from flask_sqlalchemy import *
from passlib.hash import sha256_crypt

app = Flask(__name__)

BASE_DIR = app.root_path
conf_d = yaml.load(open(os.path.join(BASE_DIR,"config.yml")))
app.secret_key = eval(conf_d['secret'])
app.config['SQLALCHEMY_DATABASE_URI'] = conf_d['sql_uri']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import *
from extras import *
from urls import *
import helpers

app.jinja_env.globals.update(helpers=helpers)

if __name__ == "__main__":
	app.env = "development"
	app.jinja_env.auto_reload = True
	app.debug = True
	app.run('0.0.0.0')