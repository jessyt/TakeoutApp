from CustomerReviewModel import CustomerReviewModel, MenuItemReviewModel

class service:
    def __init__(self):
        self.customerReview = CustomerReviewModel()
        self.menuItemReview = MenuItemReviewModel()

    def get_all_menu_reviews(self):
        return self.menuItemReview.get_all_menu_reviews()
    
    def create_menu_review(self,params):
        return self.menuItemReview.create_menu_review(params)    

    def get_all_customer_reviews(self):
        return self.customerReview.get_all_customer_reviews(id)  
    
    def create_customer_review(self, params):
        return self.customerReview.create_customer_review(params)  
