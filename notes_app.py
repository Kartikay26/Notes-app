import os, sys
import yaml
from redis import StrictRedis
from flask import *

app = Flask(__name__)

r = StrictRedis()
BASE_DIR = app.root_path
conf_d = yaml.load(open(os.path.join(BASE_DIR,"config.yml")))
app.secret_key = eval(conf_d['secret'])

from urls import *
import helpers

app.jinja_env.globals.update(helpers=helpers)

if __name__ == "__main__":
	app.env = "development"
	app.jinja_env.auto_reload = True
	app.debug = True
	app.run('0.0.0.0')