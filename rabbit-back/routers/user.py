from flask import Blueprint, request, jsonify
from controleur.user import create_user, select_user, select_all_user
user_blueprint = Blueprint("user", __name__)

@user_blueprint.route("/users/", methods=["GET"])
def send_select_all_user():
    results = select_all_user()
    return jsonify(results)

@user_blueprint.route("/user/", methods=["POST"])
def send_create_user():
    user_data = request.json
    results = create_user(user_data)
    return jsonify(results)

@user_blueprint.route("/user/<id>/", methods=["GET"])
def send_select_user(id):
    results = select_user(id)
    return jsonify(results)
