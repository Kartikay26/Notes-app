from notes_app import *

@app.route('/contents/')
def contents():
	pages = Page.query.all()
	return render_template("contents.html", pages=pages)