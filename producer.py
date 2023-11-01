import pika

from faker import Faker

from sender_mail.database.models import Contact

fake = Faker()
credentials = pika.PlainCredentials(username='sqvsmbzo', password='Xgee9pGGP9o94HNk0myQWyIxn3aw_OqC')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='puffin-01.rmq2.cloudamqp.com', 
                                                               port=5672, 
                                                               credentials=credentials, 
                                                               virtual_host='sqvsmbzo'))
channel = connection.channel()

channel.exchange_declare(exchange='contact_services', exchange_type='direct')
channel.queue_declare(queue='contact', durable=True)
channel.queue_bind(exchange='contact_services', queue='contact')



def main():
    for i in range(100):
        contact = Contact(fullname=fake.name(), email=fake.email()).save()

        channel.basic_publish(exchange='contact_services',
                              routing_key='contact',
                              body=str(contact.id).encode(),
                              properties=pika.BasicProperties(delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE))
    connection.close()


if __name__ == '__main__':
    main()

