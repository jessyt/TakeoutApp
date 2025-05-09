import sqlite3

class CustomerReviewSchema:
    def __init__(self):
        self.conn = sqlite3.connect('CustomerReview.db')
        self.create_customer_review_table()
        self.create_menu_item_review_table()

    
    def __del__(self):
        # body of destructor
        self.conn.commit()
        self.conn.close()

    def create_customer_review_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS "CustomerReview" (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        UserFK INTEGER,
        Rating INTEGER,
        Description Text
        );
        """
        self.conn.execute(query)
    
    def create_menu_item_review_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS "MenuItemReview" (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        MenuItemFK INTEGER,
        Rating INTEGER,
        Description Text
        );
        """
        self.conn.execute(query)
 
class MenuItemReviewModel:
    TABLENAME = "MenuItemReview"

    def __init__(self):
        self.conn = sqlite3.connect('CustomerReview.db')
        self.conn.row_factory = sqlite3.Row

    def __del__(self):
        # body of destructor
        self.conn.commit()
        self.conn.close()

    def get_all_menu_reviews(self):
        query = f"SELECT * from {self.TABLENAME}"
        result_set = self.conn.execute(query).fetchall()
        print(result_set)
        result = [{column: row[i]
            for i, column in enumerate(result_set[0].keys())}
            for row in result_set]
        return result    
    
    def create_menu_review(self, params):
        query = f'insert into {self.TABLENAME} (MenuItemFK, Rating, Description) values ({params.get("MenuItemFK")},{params.get("Rating")}, "{params.get("Description")}");'
        print(query)
        result = self.conn.execute(query)
        print(result)
        return f'Successfully created new Menu review'
    
    def get_menu_item_review_based_on_id(self, menu_id):
        query = f"SELECT * from {self.TABLENAME} where MenuItemFK = {menu_id}"
        result_set = self.conn.execute(query).fetchall()
        print(result_set)
        result = [{column: row[i]
            for i, column in enumerate(result_set[0].keys())}
            for row in result_set]
        return result    
  
class CustomerReviewModel:
    TABLENAME = "CustomerReview"

    def __init__(self):
        self.conn = sqlite3.connect('CustomerReview.db')
        self.conn.row_factory = sqlite3.Row

    def __del__(self):
        # body of destructor
        self.conn.commit()
        self.conn.close()

    def get_all_customer_reviews(self):
        query = f"SELECT * from {self.TABLENAME}"
        result_set = self.conn.execute(query).fetchall()
        print(result_set)
        result = [{column: row[i]
            for i, column in enumerate(result_set[0].keys())}
            for row in result_set]
        return result    
    
    def create_customer_review(self, params):
        query = f'insert into {self.TABLENAME} (UserFK, Rating, Description) values ({params.get("UserFK")},{params.get("Rating")}, "{params.get("Description")}");'
        print(query)
        result = self.conn.execute(query)
        print(result)
        return f'Successfully created new customer review'
  