import pika
import time


# properites:     
# ntent_type="text/plain",
# content_encoding="gzip",
# timestamp=10000000,
# expiration=str(time.time()),
# delivery_mode=2 ,#it say ,save the data on Disk(2) if lose you accese to it or in Ram(1) temporary,]
# user_id="10" 

credentials = pika.PlainCredentials("guest","guest")
connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost",credentials=credentials))

channel = connection.channel()

# RounRobin when the connect with rabbitmq ,the rabbit come and send all request Distribution to all service suddenly
# But we dont want set all request sudenly and i want set one one
channel.basic_qos(prefetch_count=1)


# just send for One Consumer if you want send for any queue you should learn Exchnage
channel.queue_declare(queue='one')

channel.basic_publish(exchange='',routing_key="one",body="Hello Python",properties=pika.BasicProperties(headers={"name":"afshin"}))
print("Sending is succuess ...!")


channel.queue_declare(queue='two')

channel.basic_publish(exchange='',routing_key="two",body="Hello NodeJs")
print("Sending is succuess ...!")



# Exchange ==> fanout<all queue>
channel.exchange_declare(exchange="logs",exchange_type="fanout")
channel.basic_publish(exchange="logs",routing_key="",body="it is for all")

#



print("Sending is succuess ...!")

connection.close()