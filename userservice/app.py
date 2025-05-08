from flask import Flask, request, jsonify
from service import service
from UserManagementModel import UserManagementSchema
import json
app = Flask(__name__)

@app.after_request
def add_headers(response):
    response.headers['Access-Control-Allow-Origin'] = "*"
    response.headers['Access-Control-Allow-Headers'] = "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With"
    response.headers['Access-Control-Allow-Methods']= "POST, GET, PUT, DELETE, OPTIONS"
    return response

@app.route("/")
def hello():
    return "User Service Says Hello!"

@app.route("/CreateUser", methods=["POST"])
def CreateUser():
    return jsonify(service().create_user(request.get_json()))

@app.route("/Users/<user_id>", methods=["GET"])
def GetUserById(user_id):
    return jsonify(service().get_user_by_id(user_id))

@app.route("/Users", methods=["GET"])
def GetUserById():
    return jsonify(service().get_all_users())

if __name__ == "__main__":
    UserManagementSchema()
    app.run(host='0.0.0.0', port=5003)
