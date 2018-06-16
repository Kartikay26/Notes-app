from notes_app import *
from functools import wraps

def login_required(func):
	# Decorator
	@wraps(func)
	def f_ret(*args,**kwargs):
		if 'logged_in' in session and session['logged_in']:
			return func(*args,**kwargs)
		else:
			session['logged_in'] = False
			flash("Login required to access that page")
			#redirect_to_login_page with continue argument
			return redirect(url_for('login',cont=func.__name__))
	return f_ret