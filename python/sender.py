import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))

channel = connection.channel()
# just send for One Consumer if you want send for any queue you should learn Exchnage
channel.queue_declare(queue='one')

channel.basic_publish(exchange='',routing_key="one",body="Hello Python")
print("Sending is succuess ...!")


channel.queue_declare(queue='two')

channel.basic_publish(exchange='',routing_key="two",body="Hello NodeJs")
print("Sending is succuess ...!")
connection.close()