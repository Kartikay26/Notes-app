import os, sys

import yaml

from redis import StrictRedis

from flask import *

app = Flask(__name__)

r = StrictRedis()

BASE_DIR = app.root_path

conf_d = yaml.load(open(os.path.join(BASE_DIR,"config.yml")))

app.secret_key = eval(conf_d['secret'])