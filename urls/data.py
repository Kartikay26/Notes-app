from config import *

@app.route('/data/<path:url>')
def raw_data(url):
	# TODO: make sure file exists and is md or csv or whatever
	text = open(os.path.join(BASE_DIR,'data/'+url)).read()
	resp = make_response(text,{'Content-Type':'text/plain'})
	return resp