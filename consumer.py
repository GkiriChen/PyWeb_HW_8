import pika
import time


from sender_mail.database.models import Contact


credentials = pika.PlainCredentials(username='sqvsmbzo', password='Xgee9pGGP9o94HNk0myQWyIxn3aw_OqC')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='puffin-01.rmq2.cloudamqp.com', 
                                                               port=5672, 
                                                               credentials=credentials,
                                                               virtual_host='sqvsmbzo'))
channel = connection.channel()

channel = connection.channel()

channel.queue_declare(queue='contact', durable=True)


def callback(ch, method, properties, body):
    pk = body.decode()
    contact = Contact.objects(id=pk, delivered=False).first()
    if contact:
        send_email(contact.fullname, contact.email)
        contact.update(set__delivered=True)
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='contact', on_message_callback=callback)


def send_email(full_name, email):
    print(f'Надсилаємо email до {full_name} ({email})...')
    # Ваш код для надсилання email тут
    time.sleep(1)
    print(f'Email надіслано до {full_name} ({email}).')


if __name__ == '__main__':
    channel.start_consuming()