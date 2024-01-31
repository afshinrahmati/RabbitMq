import * as  amqp from "amqplib/callback_api";

const optionMq = {
    protocol: 'amqp',
    hostname: 'localhost',
}
amqp.connect(optionMq, (error, connection) => {
    if (error) { console.log(error); throw error; };

    connection.createChannel((errorConnet, channel) => {

        if (errorConnet) { console.log(errorConnet); throw errorConnet; }


        const queueName = "two";
        channel.assertQueue(queueName, { durable: false });
        console.log(' [*] Waiting for messages in %s. To exit press CTRL+C', queueName);

        channel.consume(queueName, (msg) => {
            console.log(' [x] Received %s', msg.content.toString());
            channel.ack(msg);

        }, { noAck: false });

    })
})
