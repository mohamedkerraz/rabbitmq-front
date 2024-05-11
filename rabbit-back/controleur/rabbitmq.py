from modele.rabbitmq import RabbitMQ
import re
import os

REQUIRED_KEYS = ["title","body","author"]
my_rabbitMQ = RabbitMQ(
    server = os.environ.get('RABBITMQ_SERVER'),
    username = os.environ.get('RABBITMQ_USERNAME'),
    password = os.environ.get('RABBITMQ_PASSWORD')
)

def create_queue(queue_name):
    validity, message = is_valid_queue_name(queue_name)
    if not validity:
        return {
            "code": 400,
            "message": message,
            "success": False
        }
    return my_rabbitMQ.create_queue(queue_name)

def delete_queue(queue_name):
    validity, message = is_valid_queue_name(queue_name)
    if not validity:
        return {
            "code": 400,
            "message": message,
            "success": False
        }
    return my_rabbitMQ.delete_queue(queue_name)


def post_message(queue_name,message_data):
    validity, message = is_valid_queue_name(queue_name)
    if not validity:
        return {
            "code": 400,
            "message": message,
            "success": False
        }
    if not isinstance(message_data, dict):
        return {
            "code": 400,
            "message": "Error: message_data must be a valid json dict",
            "success": False
        }
    validity, message = is_valid_message_dict(message_data)
    if not validity:
        return {
            "code": 400,
            "message": message,
            "success": False
        }
    return  my_rabbitMQ.post_message(queue_name,message_data)

def is_valid_queue_name(queue_name):
    if not isinstance(queue_name, str):
        return False, "Error: queue_name must be a valid string"
    if len(queue_name) > 255:
        return False, "Error: queue_name too long. Max length: 255"
    
    if not re.match(r'^[a-zA-Z0-9\-_.\/]+$', queue_name):
        return False, "Error: queue_name contains invalid chars"
    
    return True, None

def is_valid_message_dict(message_data):
    for key in message_data:
        if not isinstance(message_data[key], str):
            return False, "Error: message_data values must be string"
    for required in REQUIRED_KEYS:
        if not required in message_data:
            return False, f"Error: key '{required}' must be define in message_data"
    return True, None
