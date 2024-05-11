import pika
import uuid
import datetime
import json

class RabbitMQ:
    def __init__(self,server,username,password):
        self.username = username
        self.password = password
        self.server = server
        self.connection = None

    def connect(self):
        credentials = pika.PlainCredentials(self.username, self.password)
        parameters = pika.ConnectionParameters(self.server, credentials=credentials)
        self.connection = pika.BlockingConnection(parameters)

    def close(self):
        self.connection.close()

    def create_queue(self,queue_name):
        try:
            self.connect()
            channel = self.connection.channel()
            channel.queue_declare(queue=queue_name)
            self.close()
            return {
                "code": 201,
                "queue_name": queue_name,
                "message": "Queue created",
                "success": True
            }
        except Exception as exp:
            return {
                "code": 500,
                "message": f"Error while creating queue : {exp}",
                "success": False
            }

    def delete_queue(self,queue_name):
        try:
            self.connect()
            channel = self.connection.channel()
            channel.queue_delete(queue=queue_name)
            self.close()
            return {
                "code": 200,
                "message": "Queue deleted",
                "success": True
            }
        except Exception as exp:
            return {
                "code": 500,
                "message": f"Error while deleting queue : {exp}",
                "success": False
            }

    def post_message(self,queue_name,message_data):
        try:
                        
            now = datetime.datetime.now()
            timestamp = now.timestamp()
            message = {
                "messageId": str(uuid.uuid4()),
                "eventType": "text_message",
                "timestamp": timestamp,
                "data": message_data
            }
            message = json.dumps(message)
        except Exception as exp:
            return {
                "code": 500,
                "message": f"Error while formating message : {exp}",
                "success": False
            }
        try:
            self.connect()
            channel = self.connection.channel()
            channel.basic_publish(exchange='', routing_key=queue_name, body=message)
            self.close()
            return {
                "code": 201,
                "message": "Message posted",
                "success": True
            }
        except Exception as exp:
            return {
                "code": 500,
                "message": f"Error while posting message : {exp}",
                "success": False
            }