from notes_app import *

@app.route('/login',methods=['POST','GET'])
def login():
	if request.method == "GET":
		return render_template("login.html")
	else:
		username = request.form['username']
		password = request.form['password']
		cont = '/dashboard'
		# check_login
		# use database here
		user = User.query.filter_by(username=username).first()
		if not(user):
			flash("This user does not exist!")
			return redirect('/login')
		password_correct = sha256_crypt.verify(password, user.password)
		if not(password_correct):
			flash("Password does not match! Access denied. <a href=\"#\">Forgot Password?</a>")
			return redirect('/login')
		# move to continue or default
		flash("Logged in successfully.")
		session['username'] = username
		session['u_id'] = user.u_id
		session['logged_in'] = True
		return redirect(cont)

@app.route('/register',methods=["GET","POST"])
def register():
	if request.method == "GET":
		return render_template("register.html")
	else:
		username = request.form['username']
		password = request.form['password']
		email = request.form['email']
		username = request.form['username']
		for ch in username:
			if not (ch.isalpha() or ch.isdigit()):
				flash("Invalid Username!")
				return redirect('/register')
		if User.query.filter_by(username=username).first():
			flash("Username already taken, sorry!")
			return redirect('/register')
		else:
			password = request.form['password']
			hashed_password = sha256_crypt.hash(password)
			email = request.form['email']
			user = User(username=username, password=hashed_password, email=email)
			session['username'] = username
			session['u_id'] = user.u_id
			session['logged_in'] = True
			db.session.add(user)
			db.session.commit()
			db.session.close()
			flash("User created successfully!")
			return redirect("/dashboard")

@app.route('/logout')
def logout():
	session['username'] = None
	session['u_id'] = None
	session['logged_in'] = False
	return redirect(request.referrer or '/')