# RabbitMq
How work rabbitMQ? RabbitMq is a MessageBrocker.
docker run -d --name my-rabbit -p 5672:5672 -p 15672:15672 rabbitmq:3.13-management
# what is messageBrocker ?
A message broker is software that enables applications, systems and services to communicate with each other and exchange information.
it is an intermediary computer program that create communication between system or application by managing the transfer of the data(messages) between them.
* we set for all operation 

# Message broker models:
1) Publish/Subscribe (Pub/Sub):
In this message distribution pattern, often referred to as “pub/sub,” the producer of each message publishes it to a topic, and multiple message consumers subscribe to topics from which they want to receive messages. All messages published to a topic are distributed to all the applications subscribed to it. This is a broadcast-style distribution method, in which there is a one-to-many relationship between the message’s publisher and its consumers. If, for example, an airline were to disseminate updates about the landing times or delay status of its flights, multiple parties could make use of the information: ground crews performing aircraft maintenance and refueling, baggage handlers, flight attendants and pilots preparing for the plane’s next trip, and the operators of visual displays notifying the public. A pub/sub messaging style would be appropriate for use in this scenario.
In this model, publishers send messages to a topic, and subscribers receive messages from that topic.
Publishers are not aware of the subscribers, and subscribers are not aware of the publishers.
Subscribers can receive messages even if they were not active at the time of publication, as messages are typically persisted until delivered.
* Apache Kafka: Kafka is a distributed streaming platform that supports the pub/sub model. It uses topics to which producers publish messages, and consumers subscribe to receive messages from those topics.
* RabbitMQ: RabbitMQ is a messaging broker that supports various messaging patterns, including pub/sub. It uses exchanges to route messages to queues based on subscription bindings.

2) Point-to-Point (P2P):
This is the distribution pattern utilized in message queues with a one-to-one relationship between the message’s sender and receiver. Each message in the queue is sent to only one recipient and is consumed only once. Point-to-point messaging is called for when a message must be acted upon only one time. Examples of suitable use cases for this messaging style include payroll and financial transaction processing. In these systems, both senders and receivers need a guarantee that each payment will be sent once and once only.

In this model, messages are sent from a sender (producer) to a specific recipient (consumer), known as a queue.
Each message is consumed by exactly one consumer.
Once a message is consumed, it is typically removed from the queue.
* Apache ActiveMQ: ActiveMQ is an open-source message broker that supports the point-to-point messaging model. It uses queues, where producers send messages to and consumers receive messages from.
3) Request/Response:
This model involves a sender (client) sending a request message to a receiver (server), which processes the request and sends a response message back to the sender.
The sender typically waits for a response before continuing its operation.
* gRPC: gRPC is a high-performance RPC (Remote Procedure Call) framework developed by Google. It enables request/response communication between distributed systems using Protocol Buffers as the interface definition language (IDL).
# Message brokers vs. APIs:

What is a message broker?
A message broker is software that enables applications, systems and services to communicate with each other and exchange information.

The message broker does this by translating messages between formal messaging protocols. This allows interdependent services to “talk” with one another directly, even if they were written in different languages or implemented on different platforms.

Message brokers are software modules within messaging middleware or message-oriented middleware (MOM) solutions. This type of middleware provides developers with a standardized means of handling the flow of data between an application’s components so that they can focus on its core logic. It can serve as a distributed communications layer that allows applications spanning multiple platforms to communicate internally.

Message brokers can validate, store, route, and deliver messages to the appropriate destinations. They serve as intermediaries between other applications, allowing senders to issue messages without knowing where the receivers are, whether or not they are active, or how many of them there are. This facilitates decoupling of processes and services within systems.

In order to provide reliable message storage and guaranteed delivery, message brokers often rely on a substructure or component called a message queue that stores and orders the messages until the consuming applications can process them. In a message queue, messages are stored in the exact order in which they were transmitted and remain in the queue until receipt is confirmed.

Asynchronous messaging refers to the type of inter-application communication that message brokers make possible. It prevents the loss of valuable data and enables systems to continue functioning even in the face of the intermittent connectivity or latency issues common on public networks. Asynchronous messaging guarantees that messages will be delivered once (and once only) in the correct order relative to other messages.

Message brokers may comprise queue managers to handle the interactions between multiple message queues, as well as services providing data routing, message translation, persistence, and client state management functionalities.

Guide
Guide to enterprisewide intelligent automation
Learn how intelligent automation can make your business operations a competitive advantage.

Related content
Register for the guide on observability

Message broker models
Message brokers offer two basic message distribution patterns or messaging styles:

Point-to-point messaging: This is the distribution pattern utilized in message queues with a one-to-one relationship between the message’s sender and receiver. Each message in the queue is sent to only one recipient and is consumed only once. Point-to-point messaging is called for when a message must be acted upon only one time. Examples of suitable use cases for this messaging style include payroll and financial transaction processing. In these systems, both senders and receivers need a guarantee that each payment will be sent once and once only.
Publish/subscribe messaging: In this message distribution pattern, often referred to as “pub/sub,” the producer of each message publishes it to a topic, and multiple message consumers subscribe to topics from which they want to receive messages. All messages published to a topic are distributed to all the applications subscribed to it. This is a broadcast-style distribution method, in which there is a one-to-many relationship between the message’s publisher and its consumers. If, for example, an airline were to disseminate updates about the landing times or delay status of its flights, multiple parties could make use of the information: ground crews performing aircraft maintenance and refueling, baggage handlers, flight attendants and pilots preparing for the plane’s next trip, and the operators of visual displays notifying the public. A pub/sub messaging style would be appropriate for use in this scenario.

Message brokers in cloud architectures
Cloud-native applications are built to take advantage of the inherent benefits of cloud computing, including flexibility, scalability, and rapid deployment. These applications are made up of small, discrete, reusable components called microservices. Each microservice is deployed and can run independently of the others. This means that any one of them can be updated, scaled, or restarted without affecting other services in the system. Often packaged in containers, microservices work together to comprise a whole application, though each has its own stack, including a database and data model that may be different from the others.

Microservices must have a means of communicating with one another in order to operate in concert. Message brokers are one mechanism they use to create this shared communications backbone.

Message brokers are often used to manage communications between on-premises systems and cloud components in hybrid cloud environments. Using a message broker gives increased control over interservice communications, ensuring that data is sent securely, reliably, and efficiently between the components of an application. Message brokers can play a similar role in integrating multicloud environments, enabling communication between workloads and runtimes residing on different platforms. They’re also well suited for use in serverless computing, in which individual cloud-hosted services run on demand on a per-request basis.

Message brokers vs. APIs
REST APIs are commonly used for communications between microservices. The term Representational State Transfer (REST) defines a set of principles and constraints that developers can follow when building web services. Any services that adhere to them will be able to communicate via a set of uniform shared stateless operators and requests. Application Programming Interface (API) denotes the underlying code that, if it conforms to REST rules, allows the services to talk to one another.

REST APIs use Hypertext Transfer Protocol (HTTP) to communicate. Because HTTP is the standard transport protocol of the public Internet, REST APIs are widely known, frequently used, and broadly interoperable. HTTP is a request/response protocol, however, so it is best used in situations that call for a synchronous request/reply. This means that services making requests via REST APIs must be designed to expect an immediate response. If the client receiving the response is down, the sending service will be blocked while it awaits the reply. Failover and error handling logic should be built into both services.

Message brokers enable asynchronous communications between services so that the sending service need not wait for the receiving service’s reply. This improves fault tolerance and resiliency in the systems in which they’re employed. In addition, the use of message brokers makes it easier to scale systems since a pub/sub messaging pattern can readily support changing numbers of services. Message brokers also keep track of consumers’ states.
### Message Queue:
• a message broker often operates on the concept of a message Queue.
• Application or Service send messages to a queue and other application can retrieve and process those message from the queue.
• Queues provide a way for different parts of a system to communicate asynchronously And decoupling the producer(those sending messages) and Consumers (those receiving and processing messages)

## What is Exchange:
we are not send message on queue and we send message on Exchange  
In the context of message queues, particularly in systems like RabbitMQ or Apache Kafka, an exchange is a fundamental component responsible for receiving messages from producers and routing them to message queues based on specific rules, known as bindings.

When a message is sent to an exchange, it doesn't immediately land in a queue. Instead, the exchange examines the message's routing key and other properties, and then routes it to one or more queues based on rules defined by bindings. These rules determine which queues should receive the message based on criteria such as routing keys, message attributes, or patterns.

Exchanges come in different types, each with its own routing algorithm:

1. **Direct Exchange**: Routes messages to queues based on an exact match between the routing key and the binding key. <set the name of the queue OneName>

2. **Fanout Exchange**: Routes messages to all queues bound to it, regardless of the routing key.<set on all the queue>

3. **Topic Exchange**: Routes messages to queues based on wildcard matching of the routing key.<set the names of the queue multiName>

4. **Headers Exchange**: Routes messages based on message header attributes rather than the routing key.<set the names of the queue like json>

The exchange acts as a mediator between producers and queues, ensuring that messages are delivered to the appropriate destinations based on the defined routing rules. It abstracts the complexity of message routing from producers and allows for flexible and dynamic message routing within the system.
* docker exec 14 rabbitmqctl list_exchanges
## for create Exchange(declar):
create exchange you should use the declar:
1) docker exec -it 14 rabbitmqadmin declare exchange name=send_email_events --vhost=customers  type=topic -u afshin -p 123456 durable=true
if  rabbitmqadmin is error you can use:
1.1) curl -i -u afshin:123456 -H "content-type:application/json" -XPUT http://localhost:15672/api/exchanges/customers/send_email_events -d'{"type":"topic","durable":true}'
after the create you should give the permission for the Exchange the you create.
## DELETE exchnage
1) docker exec 14 rabbitmqctl list_exchanges
2) rabbitmqctl delete_exchange <exchange_name>

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


## what is exclusive:
when you want to ensure that only a single consumer is processing messages from a queue.
1) true ==>  it means that only the connection that created the queue can access and use it. Once the connection that declared the queue is closed (either intentionally or due to a failure), the queue will be deleted. true means that only the connection that created the consumer can consume messages from the queue. If another connection attempts to consume from the same queue, it will receive an error.
2) false ==> 
## What is Ack:
when the consumer reciev the data from Queue say to producer i get it and you can delete it from your self
* befor you dont set it in your code:
    * docker exec 149 rabbitmqctl list_queues <the receiev should off>
## What is Vhost:
Virtual hosting is a method for hosting multiple domain names on a single server. 
Default Virtual Host
    * hostName:"/"
    * username:"guest",pass:"guest"
rabbitmqctl add_user <username> <password>
rabbitmqctl add_vhost my_vhost
rabbitmqctl set_permissions -p <vhost_name> <username> ".*" ".*" ".*"

2) rabbitmqctl:
* it is for  managing RabbitMq nodes   and add user ,....
2.1) Add user in RabbitMq:<LIST>
*  docker exec 14 rabbitmqctl list_users
for adding:
1) u can go to localhost:15672 and step Admin and add user.
2) docker exec 14 rabbitmqctl add_user "afshin" "1234".
2) give Access_and_Permissions[https://www.rabbitmq.com/management.html] => docker exec 14 rabbitmqctl set_user_tags "afshin" administrator.
2) give for which vHost ==> docker exec 14 rabbitmqctl set_permissions -p "/" "afshin" ".*" ".*" ".*" ==> 1) * ==> config ,Write,Read

DELETE USER ==>
1) docker exec 14 rabbitmqctl delete_user "afshin".
## what is durable:
if a queue is not durable,all messages will be lost if RabbitMQ is shut down for any reason.
for test you can write a code and in code you can specified it and after that: docker restart rabbitmq
if durable is not True all message is destroy.
## What is RoundRobin:
it is look like the Load Balancing.
it Distribution the request to multi service .
## What is reply_to , correlation_id:
Both of them shoudl set on header.
1) reply_to==> it is indentify after the server get the request and the value where set on the queue.
2) correlation_id ==> each request has unique Id that name is correlation Id.
## What is reply_to , correlation_id:

## Dependency

1. yarn add @types/express @types/node pm2 typescript
2. install RabbitMq
    2. for use in Javascript ==> npm install amqplib
    2. for use in Golang ==> python3 -m pip install pika --upgrade
    2. for use in python ==> go get github.com/rabbitmq/amqp091-go



https://www.youtube.com/watch?v=Zc2mQSQXoS4&list=PLlameCF3cMEthFSEZkS2ySnjvGg9OJ85X
https://www.youtube.com/watch?v=APfWkfkjRj8

1) create user and get vhost and permission
2) create declare docker exec -it 14 rabbitmqadmin declare exchange name=send_email_events --vhost=customers  type=topic -u afshin -p 123456 durable=true 
or 2) docker exec -it 14 rabbitmqadmin declare exchange name=send_email_events --vhost=customers  type=topic -u afshin -p 123456 durable=true
if  rabbitmqadmin is error you can use:
1.1) curl -i -u afshin:123456 -H "content-type:application/json" -XPUT http://localhost:15672/api/exchanges/customers/send_email_events -d'{"type":"topic","durable":true}'

. curl -i -u afshin:afvsa9899 -H "content-type:application/json" -XPUT http://localhost:15672/api/exchanges/send/send_email_events -d'{"type":"topic","durable":true}'
.. vhost:send,declar:send_email_evevne


101) docker exec rabbitmq rabbitmqctl add_user afshin secret
<!-- <docker exec c5 rabbitmqctl list_users> -->
102) docker exec rabbitmq rabbitmqctl set_user_tags afshin administrator
103) docker exec rabbitmq rabbitmqctl delete_user guest
<!-- CREAT ViHost -->
104) docker exec rabbitmq rabbitmqctl add_vhost email-provider
$==> after you create visualHost you should give permistion and the user acess it<withPhoto>.
105) docker execr abbitmq rabbitmqctl set_permissions -p email-provider<vhostnaem Or "/"> afshin<username> ".*" ".*" ".*"
% <!-- CREAT Queue -->
106) you should create Queue <queue_declare> queue_declare in your Code declare that mean i am exist and you can count on me if i amnot i can exist automaticly
<remmeber we are not send message on queue and we are send message on exchnage so we should first create Exchnage>
% <!-- create exchnage -->
107) create Exchnage <declare> Or with your code with clinet.exchange_declare ==> docker exec c59 rabbitmqadmin declare exchange --vhost=email-provider name=email_events type=topic -u afshin -p afvsa9899 durable=true
108) now get permission to exchnage and user for topic_exchange read and write access.
docker exec c59 rabbitmqctl set_topic_permissions -p email-provider afshin email_events "^email-provider.*" "^email-provider.*" <email-provider.*> for biding name <"email-provider.create.*">
% <!-- Connect queue to exchnage with binding name=<exchnage name in> -->
109 ) with code and it happen with queue cause queue binding the exchnage
QueueBind ,queue_bind
** Exchange =biding=> Queue <Bindings: Bindings are rules that connect exchanges to queues>

110) publishing messgae or Send<for publish messaag just need exchnage and dont matter queue> and routin key define in there
<CONSUM>

*if you want create exchnage every momount you can use code exchna_declare But one time and on it better create with terminal
















کی از سوال های محبوب مصاحبه بک اند: فرق Kafka و RabbitMQ چیه؟

۱. Performance and Scalability
کافگا برای throughput بالا و horizontal scalability ساخته شده است. هرچند RabbitMQ پرفرمنس بالایی دارد وقتی throughput و حجم داده زیاد باشد کافگا مناسب تر است.

۲. Message Ordering
در RabbitMQ در یک صف ترتیب پیام ها حفظ می‌شود. در کافگا در یک پارتیشن ترتیب پیام های یک topic حفظ می‌شود اما نه در پارتیشن های مختلف.

۳. Message Priority
در RabbitMQ از اولویت پیام ها پشتیبانی می‌شود که اجازه می‌دهد پیام های با اولویت بالا زودتر پردازش شوند. کافگا از اولویت پشتیبانی نمی‌کند.

۴. Message Model
مدل پیام های RabbitMQ مبتنی بر صف است و از پروتکل AMPQ تبعیت می‌کند اما کافگا مدل لاگ توزیع شده دارد.

۵. Durability:
برای اینکه پیام ها Durable باشند یعنی اگر failure رخ دهد از بین نروند، در RabbitMQ نیاز به تنظیمات است اما کافگا به طور درونی از این مورد پشتیبانی می‌کند.

۶. Message Routing
در Rabbit برای مسیریابی پیام ها پیشرفته تر و با استفاده از exchange و binding انجام می‌شود اما در کافگا ابتدایی تر و با استفاده از topic و پارتیشن ها انجام می‌شود.

۷. Replication
در Rabbit برای replication می توان از Mirrored Queue استفاده کرد. و کافگا نیز به صورت درونی از partition replication پشتیبانی می‌کند.

8. Stream Processing
هر دو کافگا و Rabbit از پردازش Stream پشتیبانی می کنند.

9. Latency
طراحی RabbitMQ برای تاخیر کم است و در جایی که نیاز به پردازش نزدیک به realtime است، استفاده می‌شود.

10. License
لایسنس Rabbit از نوع Mozilla Public License و لایسنس کافگا از نوع 2.0 Apache است.


تمرین عملی: یک اپلیکیشن چت بنویسید که چند نمونه از بک اند بالا باشد و هر کلاینت به یک بک اند وصل شود و از طریق کافگا یا RabbitMQ بک اند ها رو با هم sync کنید.

شما در تیمتون از چه سیستم پیام رسانی توزیع شده استفاده می کنید؟ در کامنت ها برامون مزیت هاشون رو برامون بنویسید.


