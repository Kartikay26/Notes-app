from config import *

@app.route('/')
def homepage():
	return render_template("index.html")