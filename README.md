# RabbitMq
How work rabbitMQ? RabbitMq is a MessageBrocker
# what is messageBrocker ?
it is an intermediary computer program that create communication between system or application by managing the transfer of the data(messages) between them.
* we set for all operation 
### Message Queue:
• a message broker often operates on the concept of a message Queue.
• Application or Service send messages to a queue and other application can retrieve and process those message from the queue.
• Queues provide a way for different parts of a system to communicate asynchronously And decoupling the producer(those sending messages) and Consumers (those receiving and processing messages)

## What is Exchange:

In the context of message queues, particularly in systems like RabbitMQ or Apache Kafka, an exchange is a fundamental component responsible for receiving messages from producers and routing them to message queues based on specific rules, known as bindings.

When a message is sent to an exchange, it doesn't immediately land in a queue. Instead, the exchange examines the message's routing key and other properties, and then routes it to one or more queues based on rules defined by bindings. These rules determine which queues should receive the message based on criteria such as routing keys, message attributes, or patterns.

Exchanges come in different types, each with its own routing algorithm:

1. **Direct Exchange**: Routes messages to queues based on an exact match between the routing key and the binding key. <set the name of the queue OneName>

2. **Fanout Exchange**: Routes messages to all queues bound to it, regardless of the routing key.<set on all the queue>

3. **Topic Exchange**: Routes messages to queues based on wildcard matching of the routing key.<set the names of the queue multiName>

4. **Headers Exchange**: Routes messages based on message header attributes rather than the routing key.<set the names of the queue like json>

The exchange acts as a mediator between producers and queues, ensuring that messages are delivered to the appropriate destinations based on the defined routing rules. It abstracts the complexity of message routing from producers and allows for flexible and dynamic message routing within the system.

## What is Channel:

* In the context of message queue systems like RabbitMQ or Apache Kafka, a channel is a communication pathway or virtual connection between a client (producer or consumer) and a message broker (e.g., RabbitMQ server, Kafka broker). Channels are used to send and receive messages, manage acknowledgments, and control flow between the client and the message broker.
In summary, channels play a crucial role in facilitating communication and message exchange between clients (producers and consumers) and message brokers in message . * queue systems, providing a level of abstraction and control over the underlying communication processes.
You can use one Channel for everything. However, if you have multiple threads, it's suggested to use a different Channel for each thread

## What is Plugin:
* You can add some attribute like monitoring or additional AMQP ,...
1) Management Plugin 
    it is for monitoring and graphic envoirment 
* if you want to active this you should first see all list plugin in rabbitmq
1.1) docker exec 149<Id contianer> rabbitmq-plugins list
1.2) docker exec 149 rabbitmq-plugins enable rabbitmq_management
1.3) docker exec 149 rabbitmq-plugins list
    * E==> the client active it.
    * e==> the package for active is depended on other plugin and automatic rabbitmq Active it.
1.4)  docker exec 149 rabbitmq-plugins list -v.
1.5) docker exec 149 rabbitmq-plugins list -m 
* For Disable:
. docker exec 149 rabbitmq-plugins disable rabbitmq_management
## Dependency

1. yarn add @types/express @types/node pm2 typescript
2. install RabbitMq
    2. for use in Javascript ==> npm install amqplib
    2. for use in Golang ==> python3 -m pip install pika --upgrade
    2. for use in python ==> go get github.com/rabbitmq/amqp091-go



https://www.youtube.com/watch?v=Zc2mQSQXoS4&list=PLlameCF3cMEthFSEZkS2ySnjvGg9OJ85X
https://www.youtube.com/watch?v=APfWkfkjRj8