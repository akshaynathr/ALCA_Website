from flask import Flask,request,render_template,flash
from models import User
from mongoengine import connect,Q
from werkzeug import secure_filename
import os
import datetime

app=Flask(__name__)
UPLOAD_FOLDER="static/tmp/"

app.secret_key="akshay123"
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 1* 1024 *100


connect('ALCA')
 
ALLOWED_EXTENSION=set(['jpg'])



def allowed_file(filename):
	return '.' in filename and filename.rsplit('.',1)[1] in ALLOWED_EXTENSION

@app.route('/home')
@app.route('/')

def home():
	return render_template('Login.html')



@app.route('/home',methods=['POST'])
@app.route('/'   ,methods=['POST'])

def login():
	username=None
	password=None
	try:
		username=request.form['username']
		password=request.form['password']
	
	except Exception as e:
		print (e)
	 
	if username.replace(" ",'')== '':
		error="Please enter your username"

		flash(error)
		return render_template("Login.html")

	if password.replace(" ",'') == '':
		error="Please enter your password"
		flash(error)
		return render_template("Login.html")




	user=User.objects(Q(username=username) & Q (password=password) ).first()
	if user is None:
		error="It seems that the username or password you typed is wrong"
		flash(error)
		return render_template("Login.html")
	elif user.enabled == False:
		error="Sorry. Your account is not enabled yet by administrator"
		flash(error)
		return render_template("Login.html")
	else:
		return render_template("Profile.html",user=user)

 



@app.route('/register')

def reg():
	return render_template("Register.html")


@app.route('/register', methods=['POST'])

def register():
	name=None
	emailid=None
	location=None
	username=None
	regid=None
	place=None
	password=None
	phoneno=None
	telephone=None
	website=None
	business=None

	name=request.form['name']	
	emailid=request.form['emailid']
	location=request.form['location']
	username=request.form['username']
	place=request.form['place']
	password=request.form['password']
	phoneno=request.form['phoneno']
	business=request.form['business']
	telephone=request.form['telephone']
	file=request.files['file']
	website=request.form['website']
	company=request.form['company']
	address=request.form['address']

	if not username:
		error="Username field cannot be nil"
		flash(error)
		return render_template("Register.html")

	 
	
	if not file:
		error="Upload profile image"
		flash(error)
		return render_template("Register.html")
	
	if not name:
		error="Name field cannot be nil"
		flash(error)
		return render_template("Register.html")

	if not emailid:
		error="Emailid field cannot be nil"
		flash(error) 
		return render_template("Register.html")

	if not location:
		error="Location field cannot be nil"
		flash( error)
		return render_template("Register.html")
		
	if not phoneno:
		error="Phoneno field cannot be nil"
		flash( error)
		return render_template("Register.html")

	if not place:
		error="City field cannot be nil"
		flash( error)
		return render_template("Register.html")
 
	if not password:
		error="Password field cannot be nil"
		flash( error)
		return render_template("Register.html")

	if not business:
		error="Business Activity field cannot be nil"
		flash( error)
		return render_template("Register.html")

	if not telephone:
		error="Telephone field cannot be nil"
		flash( error)
		return render_template("Register.html")

	if not address:
		error="Address field cannot be nil"
		flash(error)
		return render_template("Register.html")

	if not company:
		error="Address field cannot be nil"
		flash(error)
		return render_template("Register.html")
	

	

	user=User.objects(username=username).first()
	if user is not None:
		error="Username is already registered. Please choose another username"
		flash(error)
		return render_template("Register.html")

	
	if file and allowed_file(file.filename):
		filename=username+'.jpg'
		file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
		print("Saved:")
	else:
		error="Please use a jpg image "
		flash(error)
		return render_template("Register.html")
    		 

	user=User()
	user.name=name
	user.emailid=emailid
	user.location=location
	user.username=username
	user.password=password
	user.place=place
	user.phoneno=phoneno
	user.company=company
	user.address=address
	user.regdate=str(datetime.date.today())
	user.image_id=username+'.jpg'
	user.telephone=telephone
	user.website=website
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
	return render_template("Admin2.html")

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
		if location == 'All':
			users=User.objects.all()
			return render_template("Admin_Profile.html",users=users)
		
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
		return render_template("Admin2.html")



	if regid=="adminalca123%" and password=="kl123%":
		users=User.objects.order_by('regdate')
		return render_template("Admin_Profile.html",users=users)
	else:
		flash("Wrong username or password for admin")
		return render_template("Admin2.html")



@app.route("/delete")
def delete():
	return render_template("delete.html")



@app.route("/delete",methods=["POST"])
def delete_id():
	user=None
	username=None
	username=request.form['username']
	if username.replace(" ",'')== '':
		error="Please fill valid username"
		flash(error)
		return render_template("delete.html")


	try:
		user=User.objects(username=username).first()
		
	except :
		user=None
		return ("No user")

	
	if user is None:
		error="No user found with username:"+username
		flash(error)
		return render_template("delete.html")
	else:
		error=  user.name 
		user.delete()
		 
		 
		 
		return render_template("deleted.html",name=error)


@app.route('/edit')
def edit_get():
	return render_template("Edit.html")

@app.route("/edit",methods=['POST'])
def edit():
	username=request.form['username']
	password=request.form['password']

	if not username:
		error="Enter username"
		flash(error)
		return render_template("Edit.html")


	if not password:
		error="Enter password"
		flash(error)
		return render_template("Edit.html")


	user=User.objects(Q(username=username) & Q(password=password) ).first()
	print(user)
	if  user is None:
		error="Incorrect user"
		flash(error)
		return render_template("Edit.html")
	else:

		name=request.form['name']	
		emailid=request.form['emailid']
		location=request.form['location']
		 
		place=request.form['place']
		phoneno=request.form['phoneno']
		business=request.form['business']
		telephone=request.form['telephone']
		file=request.files['file']
		website=request.form['website']
		company=request.form['company']
		address=request.form['address']


	 
	
	if  name:
		user.update(name=name)
		 
	if  emailid:
		user.update(emailid=emailid)

	if location:
		user.update(location=location)
	

	if phoneno:
		 user.update(phoneno=phoneno)

	if place:
		 user.update(place=place)
 
	if password:
		user.update(password=password)

	if  business:
		user.update(business=business)

	if telephone:
		 user.update(telephone=telephone)

	if  address:
		user.update(address=address)

	if  company:
		user.update(company=company)
	
	if file and allowed_file(file.filename):
		filename=username+'.jpg'
		file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
		print("Saved:")


	elif allowed_file(file.filename):
		error="Please use a jpg image "
		flash(error)
		return render_template("Edit.html")

		 
	

	flash("Successfully updated")


	if user is None:
		render_template("Error")
	else:
		user.reload()
		return render_template("Profile.html",user=user)


@app.route("/hjklenatble12")
def enable_get():
	return render_template("enable.html")


@app.route("/hjklenatble12",methods=['POST'])
def enable_post():
	username=request.form['username']
	admin_password=request.form['admin_password']
	regid=request.form['regid']

	if not username:
		error="Enter username"
		flash(error)
		return render_template("enable.html")

	if not admin_password:
		error="Enter Admin Password"
		flash(error)
		return render_template("enable.html")

	if not regid:
		error="Assign registration id for user"
		flash(error)
		return render_template("enable.html")

	print(username)
	try:
		user=User.objects.get(username=username)
		name=user.name
	except :
		user=None
	 
	if user is None:
		error="No user exist with this name"
		flash(error)
		return render_template('enable.html')
	if admin_password != 'kl123%':
		error="Admin password is wrong"
		return render_template("enable.html")
	user.update(enabled=True)
	user.update(regid=regid)
	user.reload()

	return render_template("enabled.html",name=user.name)

	

	



