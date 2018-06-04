from config import *

@app.route('/dashboard/')
def dashboard():
	return render_template("index.html")