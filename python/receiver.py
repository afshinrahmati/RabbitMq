import pika
credentials = pika.PlainCredentials("afshin","afvsa9899")
conection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost",credentials=credentials,virtual_host="/"))

channel = conection.channel() 


def callback(ch,method,properties,body):
    print(f'Recived {body}')
    # print(properties.headers)
    # set handi for ack that the consumenr say to producer is recive it delete the queue
    # ch.basic_ack(delivery_tag=method.delivery_tag)
#auto_ack ==> consumer : ireceive it please deleted it. 
# channel.basic_consume(queue="send_python",on_message_callback=callback,auto_ack=True)    
print("Waiting for message,to exit press ctrl+c")

# basic_consume ==> queue =from which queue you want to receive the message

# 1 ) declare exchnage exist .2) queue declar with own name .3) binding exchnage to queue <connect> 
# 4) routinKey <without fanout cause send for all and it happend in quueue declare>
# 5 ) consume

# 11 ) fanout <exchange delcare and queue declare then binding together>
# channel.exchange_declare(exchange="fanout-python",exchange_type="fanout")
#*if queue="" it create name queu automaticlay like amq.gen-Sqt7NiqenetK2WMRdUYzmQ OR queue="test" 
# result = channel.queue_declare(queue="test",exclusive=True)
# channel.queue_bind(exchange="fanout-python",queue=result.method.queue)
# print("Waiting for fanout-python ...  ")
# channel.basic_consume(queue=result.method.queue,on_message_callback=callback,auto_ack=True)
# channel.start_consuming()

#12)topic <exchange delcare and queue declare then binding together>

# channel.exchange_declare(exchange="python_topic",exchange_type="topic")
# #*if queue="" it create name queu automaticlay like amq.gen-Sqt7NiqenetK2WMRdUYzmQ OR queue="test" exclusive=True after close queue deleted
# result = channel.queue_declare(queue="",exclusive=True)
# #  for an other routin key you should create an otehr folder.routing_key="*.*.important"
# channel.queue_bind(exchange="python_topic",queue=result.method.queue,routing_key="*.*.notimportant")
# print("Waiting for python_topic ...  ")

# channel.basic_consume(queue=result.method.queue,on_message_callback=callback,auto_ack=True)


# 13 ) headers <any ==> one of them is equal please show all message {age=>23} , all ==> all the key should equal {name=> afshin , age=>23}>
# channel.exchange_declare(exchange="python_header",exchange_type="headers")
# channel.queue_declare(queue="header-all",exclusive=True)
# bind_args = {'x-match':'all','name':'afshin','age':23}
# channel.queue_bind(exchange="python_header",queue="header-all",arguments=bind_args)

# channel.basic_consume(queue="header-all",auto_ack=True,on_message_callback=callback)

# 14 ) direct

# channel.exchange_declare(exchange="pythone-direct",exchange_type="direct")
# channel.queue_declare(queue="test-topic",exclusive=True)
# # routin key in sender is red but in ther is blue so you cna not receive any thing
# channel.queue_bind(exchange="pythone-direct",queue="test-topic",routing_key="blue")
# channel.basic_consume(queue="test-topic",on_message_callback=callback,auto_ack=True)

# 15 ) exchnage to exchnage <it exhnage_binding>

channel.exchange_declare(exchange="second-exchnage" , exchange_type="fanout")
channel.queue_declare(queue="test-exchnage-to-exchnage",exclusive=True)
channel.queue_bind(exchange="second-exchnage",queue="test-exchnage-to-exchnage")

channel.basic_consume(queue="test-exchnage-to-exchnage",on_message_callback=callback,auto_ack=True)

channel.start_consuming()