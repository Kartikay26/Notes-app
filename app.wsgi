import sys
sys.path.insert(0,'/home/ubuntu/app')

activate_this = '/home/ubuntu/app/venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

from notes_app import app as application
