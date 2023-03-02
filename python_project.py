import os


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
        
# flag = True
# while(flag):
#     user_input = int(input('choose your operation \n 1- Add user \n 2- remove user \n 3- add group \n 4- remove group \n 5- show all users and groups \n 6- Exit \n INPUT : '))
    
#     if(user_input == 1):
#         user_name = User(input('Enter username : '))
#         user_name.add_user() 
#     elif(user_input == 2):
#         user_name_to_remove = User(input('Enter username to be reomved'))
#         user_name_to_remove.remove_user()
        
#     elif(user_input == 3):
#         group_name = Group(input('Enter your group name : '))
#         group_name.add_group()
#     elif(user_input == 4):
#         group_name_to_remove = Group(input('Enter your group name to be removed : ')) 
#         group_name_to_remove.remove_group()
#     elif(user_input == 5):
#         group_name_to_fetch = Group(input('Enter your group name to be removed : '))
#         group_name_to_fetch.show_all_users_and_groups()
        
#     elif(user_input == 6):
#         flag = False
#     # else:
#     #     print('')

def newUser():
    confirm = 'N'
    addPassword = 'N'
    while confirm != 'Y':
        username = input('Enter the name for the user you wish to add : ')
        print('Use the username "' + username + '" (Y/N)')
        confirm = input().upper()
        os.system("sudo adduser " + username)

    while addPassword != 'Y':
        addPassword = input('Do you want to set a password for the user?  (Y/N)').upper()
        if addPassword != 'N':
            os.system('sudo passwd' + username)
def removeUser():
    # Remove a user with home   
    confirm = 'N'
    while confirm != 'Y':
        username = input('Enter the name for the user you wish to remove : ')
        print('remove the username "' + username + '" (Y/N)')
        confirm = input().upper()
        if(confirm == 'Y'):
            os.system("sudo deluser " + username)
            print('user has been deleted')

def createGroup():
    confirm = 'N'
    while confirm != 'Y':
        gropuName = input('Enter the name for the Group you wish to create : ')
        print('Use the Group "' + gropuName + '" (Y/N)')
        confirm = input().upper()
        if(confirm == 'Y'):
            os.system("sudo addgroup " + gropuName)


def addUserToGroup():
    confirm = 'N'
    while confirm != 'Y':
        username = input('Enter the name for the user you wish to add to Group : ')
        groupName = input('Enter the group name you wish the user to be added to : ')
        print('the username : "' + username + ' and the group name is : ' + groupName + ' (Y/N)')
        confirm = input().upper()
        if(confirm == 'Y'):
            os.system("sudo usermod -aG " + groupName +" "+ username)
def removeUserFromGroup():
    confirm = 'N'
    while confirm != 'Y':
        username = input('Enter the name for the user you wish to remove from a Group : ')
        groupName = input('Enter the group name you wish the user to be removed form : ')
        print('the username : "' + username + ' and the group name is : ' + groupName + ' (Y/N)')
        confirm = input().upper()
        if(confirm == 'Y'):
            os.system("sudo deluser " + username +" "+ groupName)

def removeGroup():
    confirm = 'N'
    while confirm != 'Y':
        groupName = input('Enter the group name you wish to remove : ')
        print('Use the Group "' + groupName + '" (Y/N)')
        confirm = input().upper()
        if(confirm == 'Y'):
            os.system("sudo delgroup " + groupName)
def showUsers():
    os.system("cat /etc/passwd")
def showGroups():
    os.system('cat /etc/group')
flag = True
while(flag):
    user_input = int(input('choose your operation \n 1- Add user \n 2- remove user \n 3- add group \n 4- add user to a group \n 5- Remove user from a group \n 6- Remove group  \n 7- show all users and groups \n 8- Show all Groups \n 9- Exit \n INPUT : '))
    
    if(user_input == 1):
        newUser()
    elif(user_input == 2):
        removeUser()
        
    elif(user_input == 3):
        createGroup()
    elif(user_input == 4):
        addUserToGroup()
    elif(user_input == 5):
        removeUserFromGroup()
    elif(user_input == 6):
        removeGroup()
    elif(user_input == 7):
        showUsers()
    elif(user_input == 8):
        showGroups()
        
    elif(user_input == 9):
        flag = False
    else:
        print('In valid input')






