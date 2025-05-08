from UserManagementModel import UserManagementModel

class service:
    def __init__(self):
        self.userItem = UserManagementModel()

    def create_user(self, params):
        return self.userItem.create_user(params)
    
    def get_user_by_id(self, id):
        return self.userItem.get_user_by_id(id)
    
    def get_all_users(self):
        return self.userItem.get_all_users()
    