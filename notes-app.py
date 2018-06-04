from config import *

from urls import *

import helpers

app.jinja_env.globals.update(helpers=helpers)

if __name__ == "__main__":
	app.env = "development"
	app.jinja_env.auto_reload = True
	app.debug = True
	app.run('0.0.0.0')