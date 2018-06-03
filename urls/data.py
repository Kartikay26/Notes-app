from config import *

@app.route('/data')
def data():
	return open(os.path.join(BASE_DIR,"data/data.csv")).read()