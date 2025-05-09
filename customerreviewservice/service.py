from CustomerReviewModel import CustomerReviewModel, MenuItemReviewModel
import requests

class service:
    def __init__(self):
        self.customerReview = CustomerReviewModel()
        self.menuItemReview = MenuItemReviewModel()

    def get_all_menu_reviews(self):
        return self.menuItemReview.get_all_menu_reviews()
    
    def create_menu_review(self,params):
        return self.menuItemReview.create_menu_review(params)    

    def get_all_customer_reviews(self):
        return self.customerReview.get_all_customer_reviews()  
    
    def create_customer_review(self, params):
        return self.customerReview.create_customer_review(params)  
    
    def get_menu_item_review_based_on_menu_id(self, menu_id):
        try:
            menuItemDetail = requests.get(f"http://menuservice:5001/GetMenuItems/{menu_id}")
            
            reviews = self.menuItemReview.get_menu_item_review_based_on_menu_id(menu_id)
            return {"menuItem": menuItemDetail.json(),"Details": reviews}
        except Exception as e:
            return f'{e}'

    
