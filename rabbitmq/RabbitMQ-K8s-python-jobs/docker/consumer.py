#!/usr/bin/env python
#
# Example consumer of queue messages
#
# pip3 install -r requirements.txt
#
import argparse
import sys
import os
import pika
import signal
import logging
import time


logging.basicConfig(level=logging.INFO)


def queue_callback(channel, method, properties, body):
    if len(method.exchange):
        logging.info("\nfrom exchange '{}': {}".format(method.exchange, body.decode('UTF-8')))
    else:
        logging.info("from queue {}: {}".format(method.routing_key, body.decode('UTF-8')))
        logging.info("Processing: {}".format(body.decode('UTF-8')))
        time.sleep(30)
        logging.info("Finished processing: {}".format(body.decode('UTF-8')))
        logging.info("DONE\n")


def signal_handler(signal, frame):
    logging.info("\nCTRL-C handler, cleaning up rabbitmq connection and quitting")
    connection.close()
    sys.exit(0)


example_usage = '''====EXAMPLE USAGE=====

Connect to remote rabbitmq host
--user=guest --password=guest --host=192.168.1.200

Specify exchange and queue name
--exchange=myexchange --queue=myqueue
'''

ap = argparse.ArgumentParser(description="RabbitMQ producer",
                             epilog=example_usage,
                             formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument('--user', default="guest", help="username e.g. 'guest'")
ap.add_argument('--password', default="guest", help="password e.g. 'pass'")
ap.add_argument('--host', default="localhost", help="rabbitMQ host, defaults to localhost")
ap.add_argument('--port', type=int, default=5672, help="rabbitMQ port, defaults to 5672")
ap.add_argument('--exchange', default="", help="name of exchange to use, empty means default")
ap.add_argument('--queue', default="testqueue", help="name of default queue, defaults to 'testqueue'")
ap.add_argument('--routing-key', default="testqueue", help="routing key, defaults to 'testqueue'")
ap.add_argument('--body', default="my test!", help="body of message, defaults to 'mytest!'")
args = ap.parse_args()

while True:
    try:
        # connect to RabbitMQ
        credentials = pika.PlainCredentials(args.user, args.password)
        connection = pika.BlockingConnection(pika.ConnectionParameters(args.host, args.port, '/', credentials))
        channel = connection.channel()
        logging.info("Connection Successful")
        break
    except pika.exceptions.AMQPConnectionError:
        logging.info("Trying to connect again . . .")

channel.basic_consume(queue=args.queue, on_message_callback=queue_callback, auto_ack=False)

# capture CTRL-C
signal.signal(signal.SIGINT, signal_handler)

logging.info("Waiting for messages, CTRL-C to quit...")
logging.info("")
channel.start_consuming()
