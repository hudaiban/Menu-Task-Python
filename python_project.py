class User:
    def __init__(self, name):
        self.name = name
        
    def remove_user(self):
        print("user removed")
    def add_user(self):
        print("user added")
    
class Group:
    def __init__(self, name):
        self.name = name
        self.users = []
        # print("group added")
    
    def add_user(self, user):
        print('user added')
        # self.users.append(user)
    
    def remove_user(self, user):
        print("user Removed")
        # if user in self.users:
        #     self.users.remove(user)
    
    def add_group(self):
        print('group added')
        # self.groups.append(group)
    
    def remove_group(self):
        print("group removed")
    
    def show_all_users_and_groups(self):
        print('users and groups')
        
flag = True
while(flag):
    user_input = int(input('choose your operation \n 1- Add user \n 2- remove user \n 3- add group \n 4- remove group \n 5- show all users and groups \n 6- Exit \n INPUT : '))
    
    if(user_input == 1):
        user_name = User(input('Enter username : '))
        user_name.add_user() 
    elif(user_input == 2):
        user_name_to_remove = User(input('Enter username to be reomved'))
        user_name_to_remove.remove_user()
        
    elif(user_input == 3):
        group_name = Group(input('Enter your group name : '))
        group_name.add_group()
    elif(user_input == 4):
        group_name_to_remove = Group(input('Enter your group name to be removed : ')) 
        group_name_to_remove.remove_group()
    elif(user_input == 5):
        group_name_to_fetch = Group(input('Enter your group name to be removed : '))
        group_name_to_fetch.show_all_users_and_groups()
        
    elif(user_input == 6):
        flag = False
    # else:
    #     print('')







