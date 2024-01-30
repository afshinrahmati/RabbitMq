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

1. **Direct Exchange**: Routes messages to queues based on an exact match between the routing key and the binding key.

2. **Fanout Exchange**: Routes messages to all queues bound to it, regardless of the routing key.

3. **Topic Exchange**: Routes messages to queues based on wildcard matching of the routing key.

4. **Headers Exchange**: Routes messages based on message header attributes rather than the routing key.

The exchange acts as a mediator between producers and queues, ensuring that messages are delivered to the appropriate destinations based on the defined routing rules. It abstracts the complexity of message routing from producers and allows for flexible and dynamic message routing within the system.


1. yarn add @types/express @types/node pm2 typescript



https://www.youtube.com/watch?v=Zc2mQSQXoS4&list=PLlameCF3cMEthFSEZkS2ySnjvGg9OJ85X
https://www.youtube.com/watch?v=APfWkfkjRj8