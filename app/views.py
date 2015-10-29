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




	user=User.objects(regid=regid).first()
	if user is None:
		error="It seems that the Register id or password you typed is wrong"
		flash(error)
		return render_template("Login.html")
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
	
		return render_template("registered.html")

@app.route('/show',methods=['GET'])
def show():
	users=User.objects
	return render_template("show.html",users=users)


@app.route('/profile')

def prof():
	return render_template("Profile.html")


@app.route('/admin')

def adm():
	return render_template("Admin.html")

@app.route("/admin",methods=['POST'])
def admin():
	regid=None
	password=None
	location=None
	sort=None

	try:
		sort=request.form['sort']
	except:
		sort=None

	if sort=="sort":
		location=request.form['location']
		
		users=User.objects(location=location)
		return render_template("Admin_Profile.html",users=users)

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
		return render_template("Admin.html")



	if regid=="adminalca123%" and password=="kl123%":
		users=User.objects.all()
		return render_template("Admin_Profile.html",users=users)
	else:
		flash("Wrong username or password for admin")
		return render_template("Admin.html")



@app.route("/delete")
def delete():
	return render_template("delete.html")



@app.route("/delete",methods=["POST"])
def delete_id():
	regid=None
	regid=request.form['regid']
	try:
		user=User.objects.get(regid=regid)
	except :
		user=None
	if regid.replace(" ",'')== '':
		error="Please fill valid Registration Id"
		flash(error)
		return render_template("delete.html")
	elif user is None:
		error="No user found with Register Id:"+regid
		flash(error)
		return render_template("delete.html")
	else:
		user.delete()
		users=User.objects.all()
		return render_template("Admin_Profile.html",users=users)



