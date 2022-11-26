import pika
class RabbitMQ_:
    def __init__(self):
        #self.AMQP_URL = "amqps://pvitcmeq:DIpBs88BrrJMqHseVwVDoch54tQqYA7n@kangaroo.rmq.cloudamqp.com/pvitcmeq"
        #self.AMQP_URL = "amqps://qyskgeeu:JtKsALJnN9PVwNKb1ivAq5hH4pa2vNxJ@whale.rmq.cloudamqp.com/qyskgeeu"
        self.AMQP_URL = "amqps://hgrthuni:fNjg7F-I1H9YYJonDB3J2wCgO4mq7lE0@hawk.rmq.cloudamqp.com/hgrthuni"
        self.ROUTING_KEY = "hello"
        self.connection = pika.BlockingConnection(pika.URLParameters(self.AMQP_URL))
        self.channel = self.connection.channel()

    def send(self, message):
        self.channel.queue_declare(queue='hello') 
        self.channel.basic_publish(exchange='', routing_key=self.ROUTING_KEY, body=message) 
        print(" [x] Sent %r" % message)
        # self.connection.close()


#print(RabbitMQ_().send('hello'))
#RabbitMQ_().send("11a312906bd411ed9f655c879c9b432f")