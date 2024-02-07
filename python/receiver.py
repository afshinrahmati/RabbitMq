import pika

conection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))

channel = conection.channel()
channel.queue_declare(queue="one")


def callback(ch,method,properties,body):
    print(f'Recived {body}')
    print(properties.headers)
    # set handi for ack that the consumenr say to producer is recive it delete the queue
    # ch.basic_ack(delivery_tag=method.delivery_tag)
#auto_ack ==> consumer : ireceive it please deleted it. 
channel.basic_consume(queue="one",on_message_callback=callback,auto_ack=True)    
print("Waiting for message,to exit press ctrl+c")




# fanout

channel.exchange_declare(exchange="logs",exchange_type="fanout")

channel.start_consuming()