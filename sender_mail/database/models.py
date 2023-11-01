from mongoengine import Document
from mongoengine.fields import BooleanField, StringField
                                

import connect_db

 
class Contact(Document):
    fullname = StringField()
    email = StringField()
    delivered = BooleanField(default=False)