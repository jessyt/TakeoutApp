import sqlite3

class UserManagementSchema:
    def __init__(self):
        self.conn = sqlite3.connect('UserManagement.db')
        self.create_user_table()
    
    def __del__(self):
        # body of destructor
        self.conn.commit()
        self.conn.close()

    def create_user_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS "User" (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        FirstName Text,
        LastName Text,
        DOB Text,
        EmailAddress Text,
        PhoneNumber Text,
        Points INTEGER
        );
        """
        self.conn.execute(query)
    

class UserManagementModel:
    TABLENAME = "User"

    def __init__(self):
        self.conn = sqlite3.connect('UserManagement.db')
        self.conn.row_factory = sqlite3.Row

    def __del__(self):
        # body of destructor
        self.conn.commit()
        self.conn.close()


    def create_user(self, params):
        query = f'insert into {self.TABLENAME} (FirstName, LastName, DOB, EmailAddress, PhoneNumber, Points) values ("{params.get("FirstName")}","{params.get("LastName")}","{params.get("DOB")}","{params.get("EmailAddress")}","{params.get("PhoneNumber")}",{params.get("Points")});'
        print(query)
        result = self.conn.execute(query)
        print(result)
        return f'Successfully created New User'

    def get_user_by_id(self, id):
        query = f"SELECT * from {self.TABLENAME} where id = {id}"
        result_set = self.conn.execute(query).fetchall()
        print(result_set)
        result = [{column: row[i]
            for i, column in enumerate(result_set[0].keys())}
            for row in result_set]
        return result
    
    def get_all_users(self):
        query = f"SELECT * from {self.TABLENAME}"
        result_set = self.conn.execute(query).fetchall()
        print(result_set)
        result = [{column: row[i]
            for i, column in enumerate(result_set[0].keys())}
            for row in result_set]
        return result
 