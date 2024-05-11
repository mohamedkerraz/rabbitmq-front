from flask import Flask
from routers.rabbitmq import rabbitmq_blueprint

app = Flask(__name__)

app.register_blueprint(rabbitmq_blueprint)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8001)