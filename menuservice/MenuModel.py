import sqlite3

class MenuSchema:
    def __init__(self):
        self.conn = sqlite3.connect('Menu.db')
        self.create_menu_table()
        self.create_ingredients_table()
        self.create_menu_item_ingredients_table()
        self.create_coffee_bean_info_table()
        self.create_milk_substitutions_table()
    
    def __del__(self):
        # body of destructor
        self.conn.commit()
        self.conn.close()

    def create_menu_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS "MenuItem" (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Name Text,
        Description Text,
        MenuItemType Text,
        IsActive INTEGER,
        AllergyInfo Text,
        Points INTEGER,
        Price INTEGER,
        RoastType INTEGER FOREIGNKEY REFERENCES CoffeeBeanInfo(_id)
        );
        
        """
        self.conn.execute(query)

        query = """
        INSERT INTO MenuItem (id, Name, Description, IsActive, MenuItemType, AllergyInfo, Points, Price, RoastType)
        values (1, "Espresso", "Single Shot Espresso", 1, "Coffee", "None", 100, 3, "Medium"),
        (2, "Double Espresso", "Double Shot Espresso", 1, "Coffee", "None", 200, 5, "Medium"),
        (3, "Latte", "Double Shot Espresso with Frothed Milk", 1, "Coffee", "Contains Milk", 200, 6, "Light"),
        (4, "Americano", "Double Shot Espresso with Hot Water", 1, "Coffee", "None", 200, 5, "Medium"),
        (5, "Drip Coffee", "Drip Coffee", 1, "Coffee", "None", 100, 3, "Medium"),
        (6, "Tea", "Hot Tea", 1, "Non Coffee", "None", 100, 3, null),
        (7, "Hot Chocolate", "Hot Chocolate with Milk", 1, "Non Coffee", "None", 200, 5, null),
        (8, "Lemonade", "Iced Lemonade", 1, "Non Coffee", "None", 300, 5, null),
        (9, "Milkshake", "Vanilla Milkshake", 1, "Non Coffee", "Milk", 500, 7, null),
        (10, "Cappuccino", "Double Shot Espresso with Extra Frothed Milk", 1, "Coffee", "Milk", 200, 6, "Light"),
        (11, "Muffin", "Banana, Chocolate, or Blueberry", 1, "Treats", "Milk, Egg", 300, 3, null),
        (12, "Danish", "Blueberry or Cherry", 1, "Treats", "Milk, Egg", 350, 4, null),
        (13, "Egg and Cheese Bagel", "Bagel with egg and cheese", 1, "Food", "Egg", 500, 7, null),
        (14, "Bagel", "Served with Cream Cheese", 1, "Food", "Dairy, Egg", 500, 5, null),
        (15, "Bacon Egg and Cheese Bagel", "Bagel with egg and cheese and bacon", 1, "Food", "Egg, Pork", 500, 7, null);
        """
        self.conn.execute(query)
    
    def create_ingredients_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS "Ingredients" (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ItemName Text
        );
        """
        self.conn.execute(query)

        query = """
        INSERT INTO Ingredients (id, ItemName)
        values (1, "Coffee"),
        (2, "Milk"),
        (3, "Simple Syrup"),
        (4, "Chocolate Syrup"),
        (5, "Lemons"),
        (6, "Ice Cream"),
        (7, "Muffin"),
        (8, "Danish"),
        (9, "Bagel"),
        (10, "Egg"),
        (11, "Butter"),
        (12, "Cheese"),
        (13, "Cream Cheese"),
        (14, "Bacon"),
        (15, "Tea");
        """
        self.conn.execute(query)

    def create_menu_item_ingredients_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS "MenuItemIngredients" (
        MenuItemFK INTEGER FOREIGNKEY REFERENCES MenuItem(_id),
        IngredientItemFK INTEGER FOREIGNKEY REFERENCES Ingredients(_id)
        );
        """
        self.conn.execute(query)
        
        query = """

        INSERT INTO MenuItemIngredients
        values (1, 1),
        (2, 1),
        (3, 1),
        (4, 1),
        (3, 2),
        (5, 1),
        (6, 15),
        (7, 2),
        (7, 4),
        (8, 5),
        (8, 3),
        (9, 2),
        (9, 6),
        (10, 1),
        (10, 2),
        (11, 7),
        (12, 8),
        (13, 10),
        (13, 11),
        (13, 12),
        (15, 10),
        (15, 11),
        (15, 12),
        (14, 13),
        (14, 9);
        """
        self.conn.execute(query)


    def create_coffee_bean_info_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS "CoffeeBeanInfo" (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        RoastType Text,
        IsActive INTEGER,
        SourcedLocation Text,
        IsEspresso INTEGER
        );
        """
        self.conn.execute(query)
        
        query = """
        Insert into CoffeeBeanInfo (id, RoastType, IsActive, SourcedLocation, IsEspresso)
        values (1, "Full", 1, "Kenya", "No"),
        (2, "Medium", 1, "Columbia", "No"),
        (3, "Light", 1, "Ethiopia", "Yes");
        """
        self.conn.execute(query)

    def create_milk_substitutions_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS "MilkSubstitutions" (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        MilkType Text,
        IsActive INTEGER
        );
        """
        self.conn.execute(query)

        query = """
        Insert into MilkSubstitutions (id, MilkType, IsActive)
        values (1, "1% Dairy Milk", 1),
        (2, "Almond", 1),
        (3, "Hemp", 1),
        (4, "Oat", 1);
        """
        self.conn.execute(query)

class MenuItemModel:
    TABLENAME = "MenuItem"

    def __init__(self):
        self.conn = sqlite3.connect('Menu.db')
        self.conn.row_factory = sqlite3.Row

    def __del__(self):
        # body of destructor
        self.conn.commit()
        self.conn.close()


    def create_menu_item(self, params):
        query = f'insert into {self.TABLENAME} (Description, Name, IsActive, MenuItemType, AllergyInfo, Points, Price, RoastType) values ("{params.get("Description")}","{params.get("Name")}",{params.get("IsActive")},"{params.get("MenuItemType")}","{params.get("AllergyInfo")}",{params.get("Points")},{params.get("Price")},"{params.get("RoastType")}");'
        print(query)
        result = self.conn.execute(query)
        print(result)
        return f'Successfully created New Menu item'

    def get_menu_item_by_id(self, id):
        query = f"SELECT * from {self.TABLENAME} where id = {id}"
        result_set = self.conn.execute(query).fetchall()
        print(result_set)
        result = [{column: row[i]
            for i, column in enumerate(result_set[0].keys())}
            for row in result_set]
        return result
    
    def get_all_menu_items(self):
        query = f"SELECT * from {self.TABLENAME}"
        result_set = self.conn.execute(query).fetchall()
        print(result_set)
        result = [{column: row[i]
            for i, column in enumerate(result_set[0].keys())}
            for row in result_set]
        return result


class IngredientsModel:
    TABLENAME = "Ingredients"

    def __init__(self):
        self.conn = sqlite3.connect('Menu.db')
        self.conn.row_factory = sqlite3.Row

    def __del__(self):
        # body of destructor
        self.conn.commit()
        self.conn.close()


    def create_ingredient(self, params):
        query = f'insert into {self.TABLENAME} (ItemName) values ("{params.get("ItemName")}");'
        print(query)
        result = self.conn.execute(query)
        print(result)
        return f'Successfully created New Ingredient item'

    def get_all_ingredients(self):
        query = f"SELECT * from {self.TABLENAME}"
        result_set = self.conn.execute(query).fetchall()
        print(result_set)
        result = [{column: row[i]
            for i, column in enumerate(result_set[0].keys())}
            for row in result_set]
        return result    

class MenuItemIngredientsModel:
    TABLENAME = "MenuItemIngredients"

    def __init__(self):
        self.conn = sqlite3.connect('Menu.db')
        self.conn.row_factory = sqlite3.Row

    def __del__(self):
        # body of destructor
        self.conn.commit()
        self.conn.close()

    def get_all_menu_item_ingredients(self):
        query = f"SELECT * from {self.TABLENAME}"
        result_set = self.conn.execute(query).fetchall()
        print(result_set)
        result = [{column: row[i]
            for i, column in enumerate(result_set[0].keys())}
            for row in result_set]
        return result    
    
    def create_menu_item_ingredient(self, params):
        query = f'insert into {self.TABLENAME} (MenuItemFK,IngredientItemFK) values ({params.get("MenuItemFK")},{params.get("MenuItemFK")});'
        print(query)
        result = self.conn.execute(query)
        print(result)
        return f'Successfully created New MenuCrosswalk item'

    def get_all_menu_items_based_on_menu_pk(self, menu_id):
        query = f"SELECT * from {self.TABLENAME} where MenuItemFK = {menu_id}"
        result_set = self.conn.execute(query).fetchall()
        print(result_set)
        result = [{column: row[i]
            for i, column in enumerate(result_set[0].keys())}
            for row in result_set]
        return result    
    
class CoffeeBeanInfoModel:
    TABLENAME = "CoffeeBeanInfo"

    def __init__(self):
        self.conn = sqlite3.connect('Menu.db')
        self.conn.row_factory = sqlite3.Row

    def __del__(self):
        # body of destructor
        self.conn.commit()
        self.conn.close()

    def get_all_coffee_bean_info(self):
        query = f"SELECT * from {self.TABLENAME}"
        result_set = self.conn.execute(query).fetchall()
        print(result_set)
        result = [{column: row[i]
            for i, column in enumerate(result_set[0].keys())}
            for row in result_set]
        return result    
    
    def create_coffee_bean_info(self, params):
        query = f'insert into {self.TABLENAME} (RoastType,IsActive,SourcedLocation,IsEspresso) values ("{params.get("RoastType")}",{params.get("IsActive")}, "{params.get("SourcedLocation")}", "{params.get("IsEspresso")}");'
        print(query)
        result = self.conn.execute(query)
        print(result)
        return f'Successfully created new coffee bean info item'
  
class MilkSubstitutionsModel:
    TABLENAME = "MilkSubstitutions"

    def __init__(self):
        self.conn = sqlite3.connect('Menu.db')
        self.conn.row_factory = sqlite3.Row

    def __del__(self):
        # body of destructor
        self.conn.commit()
        self.conn.close()

    def get_all_milk_substitutions(self):
        query = f"SELECT * from {self.TABLENAME}"
        result_set = self.conn.execute(query).fetchall()
        print(result_set)
        result = [{column: row[i]
            for i, column in enumerate(result_set[0].keys())}
            for row in result_set]
        return result    
    
    def create_milk_substitution_info(self, params):
        query = f'insert into {self.TABLENAME} (MilkType,IsActive) VALUES ("{params.get("MilkType")}", {params.get("IsActive")});'
        print(query)
        result = self.conn.execute(query)
        print(result)
        return f'Successfully created new milk item'