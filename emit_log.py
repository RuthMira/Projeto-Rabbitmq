#!/usr/bin/env python
import pika
import sys

credentials = pika.PlainCredentials('usuario', 'senha')
parameters = pika.ConnectionParameters('192.168.0.168',
                                   5672,
                                   '/',
                                   credentials)

connection = pika.BlockingConnection(parameters)

channel = connection.channel()


channel.exchange_declare(exchange='logs', exchange_type='fanout')

message = ' '.join(sys.argv[1:]) or "info: Hello World!"
channel.basic_publish(exchange='logs', routing_key='', body=message)
print(f" [x] Sent {message}")
connection.close()

