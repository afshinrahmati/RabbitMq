import pika

conection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))

channel = conection.channel()
channel.queue_declare(queue="one")


def callback(ch,method,properties,body):
    print(f'Recived {body}')
#auto_ack ==> consumer : ireceive it please deleted it. 
channel.basic_consume(queue="one",on_message_callback=callback,auto_ack=True)    
print("Waiting for message,to exit press ctrl+c")

channel.start_consuming()