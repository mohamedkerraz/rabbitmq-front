from flask import Blueprint, request, jsonify
from controleur.rabbitmq import post_message
from controleur.rabbitmq import delete_queue
from controleur.rabbitmq import create_queue

rabbitmq_blueprint = Blueprint("rabbitmq", __name__)

@rabbitmq_blueprint.route("/rabbitmq/queue/", methods=["POST"])
def send_create_queue():
    results = create_queue()
    return jsonify(results)

@rabbitmq_blueprint.route("/rabbitmq/queue/<queue_name>/", methods=["DELETE"])
def send_delete_queue(queue_name):
    results = delete_queue(queue_name)
    return jsonify(results)

@rabbitmq_blueprint.route("/rabbitmq/message/<queue_name>/", methods=["POST"])
def send_post_message(queue_name):
    try:
        message_data = request.json
    except Exception as exp:
        return jsonify({
            "code": 500,
            "message": f"Error while decoding message_data : {exp}",
            "success": False
        })
    results = post_message(queue_name, message_data)
    return jsonify(results)