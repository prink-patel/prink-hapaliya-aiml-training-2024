import pika
from pika.exchange_type import ExchangeType
from pika.credentials import PlainCredentials
from constants import RABBIT_HOST, RABBIT_USERNAME, RABBIT_PASSWORD, PORT, EXCHANGE_NAME, ROUTING_KEY
from database import *
from save_image import *
import json
import logging
logger = logging.getLogger("Streaming_data")


class ConsumerClass:
    def __init__(self) -> None:
        self.db_obj = Database() #create database object
        self.save_imag = SaveImage() #create save image object
    
    # run consumer code
    def run(self):
        self.connect_rabbitmq()
        self.create_channel()
    
    # connect rabbitmq
    def connect_rabbitmq(self):
        try:
            credential = PlainCredentials(username=RABBIT_USERNAME, password=RABBIT_PASSWORD)
            parameters = pika.ConnectionParameters(
                host=RABBIT_HOST, port=PORT, credentials=credential
            )
            self.connection = pika.BlockingConnection(parameters)
            
        except Exception as e:
            logger.critical("Connection not established")
            
    # create channel
    def create_channel(self):
        channel = self.connection.channel()
        channel.exchange_declare(
            exchange=EXCHANGE_NAME, exchange_type=ExchangeType.direct
        )
        
        queue = channel.queue_declare("", exclusive=True)
        channel.queue_bind(
            exchange=EXCHANGE_NAME, queue=queue.method.queue, routing_key=ROUTING_KEY
        )

        channel.basic_consume(
            queue=queue.method.queue,
            auto_ack=False,
            on_message_callback=self.message_callback,
        )
        channel.start_consuming()
        
    # consume message
    def message_callback(self,ch, method, properties, body):
            try:
                json_data_1 = json.loads(body.decode('utf-8'))
                self.save_imag.run(json_data_1["frame"])
                data={"bbox":json_data_1["bbox"],"time":json_data_1["time"],"cam_id":json_data_1["cam_id"],}
                self.db_obj.enter("live_streaming_data",data)
                ch.basic_ack(delivery_tag=method.delivery_tag)
            except Exception as e:
                logger.critical("Data not valid formate")
