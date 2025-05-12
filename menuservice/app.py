from flask import Flask, request, jsonify
from service import service
from MenuModel import MenuSchema
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
    return "MenuService says hello world!"

### Menu Item
@app.route("/GetMenuItems/<menu_id>", methods=["GET"])
def GetMenuItemById(menu_id):
    return jsonify(service().get_menu_item_by_id(menu_id))

@app.route("/CreateMenuItem", methods=["POST"])
def CreateMenuItem():
    return jsonify(service().create_menu_item(request.get_json()))

@app.route("/GetMenuItems", methods=["GET"])
def GetAllMenuItems():
    return jsonify(service().get_all_menu_items())

### Ingredients
@app.route("/CreateIngredient", methods=["POST"])
def CreateIngredient():
    return jsonify(service().create_ingredient(request.get_json()))

@app.route("/GetIngredients", methods=["GET"])
def GetAllIngredients():
    return jsonify(service().get_all_ingredients())

### Menu Item Ingredients
@app.route("/CreateMenuItemIngredient", methods=["POST"])
def CreateMenuItemIngredient():
    return jsonify(service().create_menu_item_ingredient(request.get_json()))

@app.route("/GetMenuItemIngredients", methods=["GET"])
def GetMenuItemIngredients():
    return jsonify(service().get_all_menu_item_ingredients())

@app.route("/GetAllMenuItemsBasedOnMenuId/<menu_id>", methods=["GET"])
def GetMenuItemsBasedOnMenu(menu_id):
    return jsonify(service().get_all_menu_items_based_on_menu_pk(menu_id))

@app.route("/GetEntireMenu", methods=["GET"])
def GetEntireMenu():
    return jsonify(service().get_entire_menu())

### Coffee Bean Information
@app.route("/GetAllCoffeeBeanInfo", methods=["GET"])
def GetAllCoffeeBeanInfo():
    return jsonify(service().get_all_coffee_bean_info())

@app.route("/CreateCoffeeBeanInfo", methods=["POST"])
def CreateCoffeeBeanInfo():
    return jsonify(service().create_coffee_bean_info(request.get_json()))

## Milk Substitutions
@app.route("/GetAllMilkSubstitutionInfo", methods=["GET"])
def GetAllMilkSubstitutionInfo():
    return jsonify(service().get_all_milk_substitutions())

@app.route("/CreateMilkSubstitutionInfo", methods=["POST"])
def CreateMilkSubstitutionInfo():
    return jsonify(service().create_milk_substitution_info(request.get_json()))

if __name__ == "__main__":
    MenuSchema()
    app.run(host='0.0.0.0', port=5001)
