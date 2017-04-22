import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

while True:
	st = str(input("Falae jao: "))
	pass

	channel.basic_publish(exchange='',
	                      routing_key='hello',
	                      body=st)
	print(" [x] Sent '{}'".format(st))

connection.close()