

from mongoengine import CASCADE, Document
from mongoengine.fields import  StringField, ReferenceField, ListField

import connect_db 

class Author(Document):
    fullname = StringField(unique=True)
    born_date = StringField()
    born_location = StringField()
    description = StringField()

class Quote(Document):
    tags = ListField(StringField())
    author = ReferenceField(Author, reverse_delete_rule=CASCADE)
    quote = StringField()
