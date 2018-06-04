from config import *

@app.route('/editor/<path:url>')
def editor(url):
	title = url.split('/')[-1].title()
	title = title+" | Editor" if title != "Index" else "Home | Editor"
	return render_template("editor.html",page_path=url,page_title=title)