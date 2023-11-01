import json

from models import Author, Quote
import connect_db 

#db.createCollection("Author")

def seed_a():
    with open('authors.json') as f:
        file_content = f.read()
        templates = json.loads(file_content)


        for i in templates:
            Author(fullname = i['fullname'], 
                born_date = i['born_date'], 
                born_location = i['born_location'],
                description =  i['description']
                ).save()

def seed_q():
    with open('quotes.json') as f:
        file_content = f.read()
        templates = json.loads(file_content)

        for i in templates:
            Quote(tags = i['tags'], 
                author = Author.objects(fullname=i['author']).first(),
                quote =i['quote']
                ).save()
            
# seed_a()
# seed_q()