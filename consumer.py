from flask import Flask, jsonify
from flask_socketio import SocketIO, emit
from flask_cors import CORS
import pika

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="http://localhost:8080")
CORS(app)

# Configuration RabbitMQ
rabbitmq_credentials = pika.PlainCredentials('rabbitMQ', 'password@123')
rabbitmq_parameters = pika.ConnectionParameters('localhost', credentials=rabbitmq_credentials)

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('get_messages')
def get_messages():
    # Se connecter à RabbitMQ avec les identifiants
    connection = pika.BlockingConnection(rabbitmq_parameters)
    channel = connection.channel()

    # Déclarer la file RabbitMQ
    channel.queue_declare(queue='d118b99a-9e74-44bd-b1c0-f7a7e017e1fd')

    # Fonction callback pour la consommation des messages
    def callback(ch, method, properties, body):
        print("Message reçu:", body.decode())
        # Envoyer le message au client via WebSocket
        emit('message', body.decode())

    # Consommer les messages
    channel.basic_consume(queue='d118b99a-9e74-44bd-b1c0-f7a7e017e1fd', on_message_callback=callback, auto_ack=True)

    # Démarrer la consommation
    print("En attente de messages...")
    channel.start_consuming()

if __name__ == '__main__':
    socketio.run(app, debug=True)
