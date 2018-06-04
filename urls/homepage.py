from config import *

@app.route('/')
def homepage():
	return redirect('/notes/index')