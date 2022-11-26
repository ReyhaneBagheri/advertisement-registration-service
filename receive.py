import pika, sys, os
import projectjavad as database
import s3
import immaga
import mail

#AMQP_URL = "amqps://pvitcmeq:DIpBs88BrrJMqHseVwVDoch54tQqYA7n@kangaroo.rmq.cloudamqp.com/pvitcmeq"
#AMQP_URL = "amqps://hgrthuni:fNjg7F-I1H9YYJonDB3J2wCgO4mq7lE0@hawk.rmq.cloudamqp.com/hgrthuni"


def received():
    AMQP_URL = "amqps://hgrthuni:fNjg7F-I1H9YYJonDB3J2wCgO4mq7lE0@hawk.rmq.cloudamqp.com/hgrthuni"
    connection = pika.BlockingConnection(pika.URLParameters(AMQP_URL))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)
        id = body.decode("utf-8") 
        url='null'
        email='null'
        record=database.returnItem(str(id))
        for row in record:
            url=s3.generate_presigned_url('project-javad',row[3] )
            email= row[2]
        title=immaga.fun2(url)
        if title == 'null':
            database.updatTablestate(str(id), "-1")
            print(email)
            mail.mailgan().mailToUser(email, 'The result of the ad', 'Your ad was rejected.')
            print("1")
        else :
            database.updatTablestate(str(id), "1")
            database.updatTablecat(str(id), title)
            text= 'Your ad has been approved. '+' category of immage : ' + str(title) + ' your pic url : ' + str(url)
            print(text)
            mail.mailgan().mailToUser(email, 'The result of the ad', text)
            print("2")
    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()



            
if __name__ == "__main__":                      
    received()