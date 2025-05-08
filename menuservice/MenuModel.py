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
        IsActive INTEGER,
        MenuItemType Text,
        AllergyInfo Text,
        Points INTEGER,
        Price INTEGER,
        RoastType INTEGER FOREIGNKEY REFERENCES CoffeeBeanInfo(_id)
        );
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

    def create_menu_item_ingredients_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS "MenuItemIngredients" (
        MenuItemFK INTEGER FOREIGNKEY REFERENCES MenuItem(_id),
        IngredientItemFK INTEGER FOREIGNKEY REFERENCES Ingredients(_id)
        );
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

    def create_milk_substitutions_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS "MilkSubstitutions" (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Type Text,
        IsActive INTEGER
        );
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
        query = f'insert into {self.TABLENAME} (Description, IsActive, MenuItemType, AllergyInfo, Points, Price, RoastType) values ("{params.get("Description")}","{params.get("Name")}",{params.get("IsActive")},"{params.get("MenuItemType")}","{params.get("AllergyInfo")}",{params.get("Points")},{params.get("Price")},"{params.get("RoastType")}");'
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

    def get_all_menu_items_based_on_menu_pk(self, params):
        query = f"SELECT * from {self.TABLENAME} where MenuItemFK = {params.get('MenuItemFK')}"
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
        query = f'insert into {self.TABLENAME} (RoastType,IsActive,SourcedLocation,IsEspresso) values ("{params.get("RoastType")}",{params.get("IsActive")}, "{params.get("SourcedLocation")}", {params.get("IsEspresso")});'
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
        query = f'insert into {self.TABLENAME} (Type,IsActive) VALUES "{params.get("Type")}", {params.get("IsActive")});'
        print(query)
        result = self.conn.execute(query)
        print(result)
        return f'Successfully created new milk item'