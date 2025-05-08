from MenuModel import MenuItemModel, MilkSubstitutionsModel ,CoffeeBeanInfoModel, MenuItemIngredientsModel, IngredientsModel

class service:
    def __init__(self):
        self.menuItem = MenuItemModel()
        self.ingredients = IngredientsModel()
        self.menuItemIngredients = MenuItemIngredientsModel()
        self.coffeeBeanInfo = CoffeeBeanInfoModel()
        self.milksubstitutions = MilkSubstitutionsModel()

    def create_menu_item(self, params):
        return self.menuItem.create_menu_item(params)
    
    def get_menu_item_by_id(self, id):
        return self.menuItem.get_menu_item_by_id(id)
    
    def get_all_menu_items(self):
        return self.menuItem.get_all_menu_items()

    def create_ingredient(self, params):
        return self.ingredients.create_ingredient(params)

    def get_all_ingredients(self):
        return self.ingredients.get_all_ingredients()
    
    def get_all_menu_item_ingredients(self):
        return self.menuItemIngredients.get_all_menu_item_ingredients()

    def create_menu_item_ingredient(self, params):
        return self.menuItemIngredients.create_menu_item_ingredient(params)  

    def get_all_menu_items_based_on_menu_pk(self, menu_id):
        return self.menuItemIngredients.get_all_menu_items_based_on_menu_pk(menu_id) 
    
    def get_all_coffee_bean_info(self):
        return self.coffeeBeanInfo.get_all_coffee_bean_info() 

    def create_coffee_bean_info(self, params):
        return self.coffeeBeanInfo.create_coffee_bean_info(params) 
    
    def get_all_milk_substitutions(self):
        return self.milksubstitutions.get_all_milk_substitutions() 

    def create_milk_substitution_info(self, params):
        return self.milksubstitutions.create_milk_substitution_info(params) 
 