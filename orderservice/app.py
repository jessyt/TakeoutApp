from flask import Flask, request, jsonify
from service import service
from OrderStatusManagementModel import OrderStatusManagementSchema
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
    return "OrderService says Hello!!"

#########################
## OrderStatusManagementService
#########################
@app.route("/CreateOrder", methods=["POST"])
def CreateUser():
    return jsonify(service().create_order(request.get_json()))

@app.route("/Orders", methods=["GET"])
def GetAllOrders():
    return jsonify(service().get_all_orders())

@app.route("/Orders/<order_id>", methods=["GET"])
def GetUserById(order_id):
    return jsonify(service().get_order_by_id(order_id))

@app.route("/GetAllOrderMenuCrosswalk", methods=["GET"])
def GetAllOrderMenuCrosswalk():
    return jsonify(service().get_all_order_menu_item_crosswalk())

@app.route("/CreateOrderMenuCrosswalk", methods=["POST"])
def CreateOrderMenuCrosswalk():
    return jsonify(service().create_order_menu_crosswalk(request.get_json()))

if __name__ == "__main__":
    OrderStatusManagementSchema()
    app.run(host='0.0.0.0', port=5002)
