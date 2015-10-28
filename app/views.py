from flask import Flask,request,render_template,flash
from models import User
from mongoengine import connect,Q
app=Flask(__name__)
app.secret_key="akshay123"

connect('ALCA')


@app.route('/home')
@app.route('/')

def home():
	return render_template('Login.html')



@app.route('/home',methods=['POST'])
@app.route('/'   ,methods=['POST'])

def login():
	regid=None
	password=None
	try:
		regid=request.form['regid']
		password=request.form['password']
	
	except Exception as e:
		print (e)	
	 
	if regid.replace(" ",'')== '':
		error="Please enter your registration Id"

		flash(error)
		return render_template("Login.html")

	if password.replace(" ",'') == '':
		error="Please enter your password"
		flash(error)
		return render_template("Login.html")


	user=User.objects(Q(regid=regid) & Q(password=password)).first()
	if user is None:
		return "Not registered"
	return render_template("Profile.html",user=user)

 



@app.route('/register')

def reg():
	return render_template("Register.html")


@app.route('/register', methods=['POST'])

def register():
	name=None
	emailid=None
	location=None
	regid=None
	place=None
	password=None
	phoneno=None
	name=request.form['name']	
	emailid=request.form['emailid']
	location=request.form['location']
	regid=request.form['regid']
	place=request.form['place']
	password=request.form['password']
	phoneno=request.form['phoneno']
	print("name:%s") %{location}

	
	
	if name.replace(" ",'') == '':
		error="Name field cannot be nil"
		flash(error)
		return render_template("Register.html")

	if emailid.replace(" ",'')== '' :
		error="Emailid field cannot be nil"
		flash(error) 
		return render_template("Register.html")

	if location.replace(" ",'')== '' :
		error="Location field cannot be nil"
		flash( error)
		return render_template("Register.html")
		
	if phoneno.replace(" ",'') == '':
		error="Phoneno field cannot be nil"
		flash( error)
		return render_template("Register.html")

	if place.replace(" ",'') == '':
		error="City field cannot be nil"
		flash( error)
		return render_template("Register.html")
 
	if password.replace(" ",'') == '':
		error="Password field cannot be nil"
		flash( error)
		return render_template("Register.html")

	user=User.objects(emailid=emailid).first()
	if user is not None:
		error="Already Registered. Please Login"
		flash(error)
		return render_template("Register.html")

	else:
		user=User()
		user.name=name
		user.emailid=emailid
		user.location=location
		user.regid=regid
		user.password=password
		user.place=place
		user.phoneno=phoneno
		user.save()
	
		return "User registered"

@app.route('/show',methods=['GET'])
def show():
	users=User.objects
	return render_template("show.html",users=users)


@app.route('/profile')

def prof():
	return render_template("Profile.html")
