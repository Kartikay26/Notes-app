from notes_app import *

@app.route('/notes/<path:url>')
def browse(url):
	title = url.split('/')[-1].title()
	title = title+" | Hypernotes" if title != "Index" else "Home | HyperNotes"
	return render_template("browse.html",page_title=title,page_path=url)