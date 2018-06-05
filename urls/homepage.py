from notes_app import *

@app.route('/')
def homepage():
	return redirect('/notes/index')