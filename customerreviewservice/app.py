from flask import Flask, request, jsonify
from service import service
from CustomerReviewModel import CustomerReviewSchema
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
    return "CustomerReviewService says hello world!"

#########################
## CustomerReviewManagementService
#########################
@app.route("/CreateMenuReview", methods=["POST"])
def CreateMenuReview():
    return jsonify(service().create_menu_review(request.get_json()))

@app.route("/MenuReviews", methods=["GET"])
def GetAllMenuReviews():
    return jsonify(service().get_all_menu_reviews())

@app.route("/CreateCustomerReview", methods=["POST"])
def CreateCustomerReview():
    return jsonify(service().create_customer_review(request.get_json()))

@app.route("/CustomerReviews", methods=["GET"])
def GetAllCustomerReviews():
    return jsonify(service().get_all_customer_reviews())

@app.route("/GetMenuItemReviewBasedOnId/<menu_id>", methods=["GET"])
def GetMenuItemsBasedOnMenu(menu_id):
    return jsonify(service().get_menu_item_review_based_on_menu_id(menu_id))

@app.route("/GetRestaurantReview", methods=["GET"])
def GetRestaurantReview():
    return jsonify(service().get_restaurant_review())

if __name__ == "__main__":
    CustomerReviewSchema()
    app.run(host='0.0.0.0', port=5000)
