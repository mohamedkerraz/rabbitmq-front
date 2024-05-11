from flask import Flask, jsonify
from flask_socketio import SocketIO, emit
from flask_cors import CORS
import pika
import os

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="http://localhost:8080")
CORS(app)

rabbitmq_username = os.environ.get('RABBITMQ_USERNAME')
rabbitmq_password= os.environ.get('RABBITMQ_PASSWORD')

# Configuration RabbitMQ
rabbitmq_credentials = pika.PlainCredentials(rabbitmq_username, rabbitmq_password)
rabbitmq_parameters = pika.ConnectionParameters('localhost', credentials=rabbitmq_credentials)

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('get_messages')
def get_messages(queue_name):
    # queue_name = 'd118b99a-9e74-44bd-b1c0-f7a7e017e1fd'
    # Se connecter à RabbitMQ avec les identifiants
    connection = pika.BlockingConnection(rabbitmq_parameters)
    channel = connection.channel()

    # Déclarer la file RabbitMQ
    channel.queue_declare(queue=queue_name)

    def callback(ch, method, properties, body):
        print("Message reçu:", body.decode())
        emit('message', body.decode())

    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

    print("En attente de messages...")
    channel.start_consuming()

if __name__ == '__main__':
    socketio.run(app, debug=True)
