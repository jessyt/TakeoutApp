from OrderStatusManagementModel import OrderModel, OrderMenuCrosswalkModel
    
class service:
    def __init__(self):
        self.orderItem = OrderModel()
        self.orderMenuCrosswalkItem = OrderMenuCrosswalkModel()

    def create_order(self,params):
        return self.orderItem.create_order(params)
    
    def get_all_orders(self):
        return self.orderItem.create_order()    

    def get_order_by_id(self, id):
        return self.orderItem.get_order_by_id(id)  
    
    def create_order_menu_crosswalk(self, params):
        return self.orderMenuCrosswalkItem.create_order_menu_crosswalk(params)  

    def get_all_order_menu_item_crosswalk(self):
        return self.orderMenuCrosswalkItem.create_order_menu_crosswalk()  
        