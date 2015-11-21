from mongoengine import *




class User(Document):
	username=StringField(required=True)
	regid=StringField(default="-1")
	password=StringField(required=True)
	emailid=StringField(required=True)
	place=StringField(required=True)
	phoneno=StringField(required=True)
	name=StringField(required=True)
	location=StringField(required=True)
	telephone=StringField(required=True)
	website=StringField()
	company=StringField()
	address=StringField()
	panchayat=StringField()
	business=StringField()
	image_id=StringField()
	regdate=StringField()
	enabled=BooleanField(default=False)

	 

	@property
	def is_authenticated():
		return True
	@property
	def is_active():
		return True
	
	@property
	def is_anonymous():
		return True
	
	@property
	def get_id():
		return id 
