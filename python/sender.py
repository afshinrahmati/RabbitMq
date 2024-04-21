import pika
import time


# properites:     
# ntent_type="text/plain",
# content_encoding="gzip",
# timestamp=10000000,
# expiration=str(time.time()),
# delivery_mode=2 ,#it say ,save the data on Disk(2) if lose you accese to it or in Ram(1) temporary,]
# user_id="10" 

credentials = pika.PlainCredentials("afshin","afvsa9899")
connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost",credentials=credentials,virtual_host="/"))

channel = connection.channel()

# RounRobin when the connect with rabbitmq ,the rabbit come and send all request Distribution to all service suddenly
# But we dont want set all request sudenly and i want set one one
# channel.basic_qos(prefetch_count=1)


# just send for One Consumer if you want send for any queue you should learn Exchnage
# channel.queue_declare(queue='send_email_event')

# channel.basic_publish(exchange='',routing_key="send_email_event",body="Hello Python",properties=pika.BasicProperties(headers={"name":"afshin"}))
# print("Sending is succuess ...!")


#1) Fanout (j=just exchnage delerar) **<Dont need routinKey and Queue cauause it send to all queue> 
# channel.exchange_declare(exchange="fanout-python",exchange_type="fanout")
# channel.basic_publish(exchange="fanout-python",routing_key="",body="FanOut..Python")
# print("Sending is succuess Fanout ...!")


#2) Topic (just exchnage declare and routing_key in publish) <like path like==> red.gree.yellow>
# channel.exchange_declare(exchange="python_topic",exchange_type="topic")
# messages = {
#     'error.warning.important' : 'this is an important message',
#     'info.debug.notimportant': 'this is no important message'
# }
# for k,v in messages.items():
#     channel.basic_publish(exchange="python_topic",routing_key=k,body=v)
    
# print("send in topic ....")


#3) Headers <exchange_declare and Routin key>

# channel.exchange_declare(exchange="python_header",exchange_type="headers")
# message = "afshin Headers..."
# # any ==> es(headers={'age' : 23})) all ==> 'age' : 23 , 'name':'afshin' just age is error
# channel.basic_publish(exchange="python_header" , routing_key="" ,body=message , properties=pika.BasicProperties(headers={'age' : 23,'name':'afshin'}))
# print("send in Headers ....")


# 4) direct <just declare>
# channel.exchange_declare(exchange="pythone-direct",exchange_type="direct")
# message = "direct afshin python..."
# channel.basic_publish(exchange="pythone-direct",routing_key="red",body=message)
# print("send in direct ....")

# 5 ) exchnage to exchnage <it exhnage_binding>
channel.exchange_declare(exchange="first-exchange",exchange_type="direct")
channel.exchange_declare(exchange="second-exchnage" , exchange_type="fanout")
# first messgae go to "second-exchnage", then go to "first-exchange"
channel.exchange_bind("second-exchnage","first-exchange")
channel.basic_publish(exchange="first-exchange" , routing_key="" , body="afshin Yellow")

print("exhnage it oky .. ")


connection.close()