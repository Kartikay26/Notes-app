from notes_app import *

@app.route('/dashboard/')
def dashboard():
	return render_template("index.html")