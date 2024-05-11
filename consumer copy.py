import pika
from flask import Flask, jsonify

app = Flask(__name__)

# Configuration RabbitMQ
rabbitmq_credentials = pika.PlainCredentials('rabbitMQ', 'password@123')
rabbitmq_parameters = pika.ConnectionParameters('localhost', credentials=rabbitmq_credentials)

@app.route('/messages', methods=['GET'])
def get_messages():

    # Se connecter à RabbitMQ avec les identifiants
    connection = pika.BlockingConnection(rabbitmq_parameters)
    channel = connection.channel()

    # Déclarer la file RabbitMQ
    channel.queue_declare(queue='d118b99a-9e74-44bd-b1c0-f7a7e017e1fd')

    # Fonction callback pour la consommation des messages
    def callback(ch, method, properties, body):
        print("Message reçu:", body.decode())
        return body.decode()
        # Vous pouvez faire ce que vous voulez avec le message ici

    # Consommer les messages
    channel.basic_consume(queue='d118b99a-9e74-44bd-b1c0-f7a7e017e1fd', on_message_callback=callback, auto_ack=True)

    # Démarrer la consommation
    print("En attente de messages...")
    channel.start_consuming()

    # Réponse de l'API
    return jsonify({"message": "Subscription started"})

if __name__ == '__main__':
    app.run(debug=True)

