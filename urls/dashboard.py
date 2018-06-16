from notes_app import *

@app.route('/dashboard/')
@login_required
def dashboard():
	user = User.query.filter_by(u_id=session['u_id']).first()
	return render_template("dashboard.html",user=user)