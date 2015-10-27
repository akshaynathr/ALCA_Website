from mongoengine import *




class User(Document):
	regid=StringField(required=True)
	name=StringField(required=True)
	location=StringField(required=True)
	emailid=StringField(required=True)

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
