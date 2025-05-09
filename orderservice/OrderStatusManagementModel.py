import sqlite3

class OrderStatusManagementSchema:
    def __init__(self):
        self.conn = sqlite3.connect('OrderStatusManagement.db')
        self.create_order_table()
        self.create_order_menu_crosswalk_table()
        
    def __del__(self):
        # body of destructor
        self.conn.commit()
        self.conn.close()

    def create_order_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS "OrderTable" (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        UserId INTEGER,
        StartedTime Text,
        CompletedTime Text,
        PointTotal Integer,
        OrderStatus Text,
        TimeToComplete INTEGER,
        TotalCost Integer
        );

        """
        self.conn.execute(query)

    def create_order_menu_crosswalk_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS "OrderMenuCrosswalk" (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        MenuItemFK INTEGER,
        OrderFK INTEGER
        );
        """
        self.conn.execute(query)

class OrderModel:
    TABLENAME = "OrderTable"

    def __init__(self):
        self.conn = sqlite3.connect('OrderStatusManagement.db')
        self.conn.row_factory = sqlite3.Row

    def __del__(self):
        # body of destructor
        self.conn.commit()
        self.conn.close()


    def create_order(self, params):
        query = f'''
        INSERT INTO {self.TABLENAME}
        (UserId, StartedTime, CompletedTime, PointTotal, OrderStatus, TimeToComplete, TotalCost)
        VALUES (
            {params.get("UserId")},
            "{params.get("StartedTime")}",
            "{params.get("CompletedTime")}",
            {params.get("PointTotal")},
            "{params.get("OrderStatus")}",
            {params.get("TimeToComplete")},
            {params.get("TotalCost")}
        );
        '''        
        print(query)
        result = self.conn.execute(query)
        print(result)
        return f'Successfully created New User'

    def get_all_orders(self):
        query = f"SELECT * from {self.TABLENAME}"
        result_set = self.conn.execute(query).fetchall()
        print(result_set)
        result = [{column: row[i]
            for i, column in enumerate(result_set[0].keys())}
            for row in result_set]
        return result
    
    def get_order_by_id(self, id):
        query = f"SELECT * from {self.TABLENAME} where id = {id}"
        result_set = self.conn.execute(query).fetchall()
        print(result_set)
        result = [{column: row[i]
            for i, column in enumerate(result_set[0].keys())}
            for row in result_set]
        return result
 
class OrderMenuCrosswalkModel:
    TABLENAME = "OrderMenuCrosswalk"

    def __init__(self):
        self.conn = sqlite3.connect('OrderStatusManagement.db')
        self.conn.row_factory = sqlite3.Row

    def __del__(self):
        # body of destructor
        self.conn.commit()
        self.conn.close()


    def create_order_menu_crosswalk(self, params):
        query = f'insert into {self.TABLENAME} (OrderFK, MenuItemFK) values ({params.get("OrderFK")},{params.get("MenuItemFK")});'
        print(query)
        result = self.conn.execute(query)
        print(result)
        return f'Successfully created New Order Menu Crosswalk item'

    def get_crosswalk_based_on_order_id(self,id):
        query = f"SELECT * from {self.TABLENAME} where OrderFK = {id}"
        result_set = self.conn.execute(query).fetchall()
        print(result_set)
        result = [{column: row[i]
            for i, column in enumerate(result_set[0].keys())}
            for row in result_set]
        return result
    
    def get_all_order_menu_item_crosswalk(self):
        query = f"SELECT * from {self.TABLENAME}"
        result_set = self.conn.execute(query).fetchall()
        print(result_set)
        result = [{column: row[i]
            for i, column in enumerate(result_set[0].keys())}
            for row in result_set]
        return result
    

 