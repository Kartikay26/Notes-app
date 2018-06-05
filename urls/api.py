from notes_app import *

import base64

@app.route('/api/save/<path:url>',methods=["POST"])
def save(url):
	file_path = os.path.join(BASE_DIR,"data/"+url)
	data = base64.b64decode(request.form['text'])
	if not os.path.exists(file_path):
		raise InvalidUsage("Cannot create new file from editor!")
	if not os.path.exists(file_path+".new"):
		open(file_path+".new",'w').write(data)
	else:
		raise InvalidUsage("Already pending review!")
	flash("Saved for review!")
	return "OK"

@app.route('/api/contents')
def get_contents():
	pass

# API ERROR HANDLING CODE
####################################################################
class InvalidUsage(Exception):
	status_code = 400
	def __init__(self, message, status_code=None, payload=None):
		Exception.__init__(self)
		self.message = message
		if status_code is not None:
			self.status_code = status_code
		self.payload = payload
	def to_dict(self):
		rv = dict(self.payload or ())
		rv['message'] = self.message
		return rv
@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
	response = jsonify(error.to_dict())
	response.status_code = error.status_code
	return response