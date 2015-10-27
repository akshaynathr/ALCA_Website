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
	emailid=None
	regid=None
	try:
		emailid=request.form['emailid']
		regid=request.form['regid']
	
	except Exception as e:
		print (e)	
	if(emailid is None):
		return "None error"

	user=User.objects(Q(emailid=emailid) & Q(regid=regid)).first()
	if user is None:
		return "Not registered"
	return render_template("profile.html",user=user)

 



@app.route('/register')

def reg():
	return render_template("Register.html")


@app.route('/register', methods=['POST'])

def register():
	name=None
	emailid=None
	location=None
	regid=None
	name=request.form['name']	
	emailid=request.form['emailid']
	location=request.form['location']
	regid=request.form['regid']
	print("name:%s") %{location}
	
	if name.replace(" ",'') == '' or name==" ":
		error="Name field cannot be nil"
		flash(error)
		return render_template("Register.html")

	if emailid.replace(" ",'')== '' or name==" ":
		error="Emailid field cannot be nil"
		flash(error) 
		return render_template("Register.html")

	if location.replace(" ",'')== '' or name==" ":
		error="Location field cannot be nil"
		flash( error)
		return render_template("Register.html")
		
	if regid.replace(" ",'') == '' or name==" ":
		error="RegId field cannot be nil"
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
		user.save()
	
		return "User registered"

@app.route('/show',methods=['GET'])
def show():
	users=User.objects
	return render_template("show.html",users=users)
