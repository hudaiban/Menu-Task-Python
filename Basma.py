import os

def show_group_users():  
    os.system("cat /etc/passwd")
         

def add_user_to_group():  
    confirm = "N"
    while confirm != "Y":
         groupname = input("Enter the name of the group: ")
         username = input("Enter the username you want to add to the group: ")
         print("use the group name '"+ groupname +"'?(yes/no)")
         confirm = input().upper()
    os.system("sudo usermod -a -G "+groupname+" "+username)
    print('user added to group')

def add_group():  
    confirm = "N"
    while confirm != "Y":
         groupname = input("Enter the name of the group to add: ")
         print("use the group name '"+ groupname +"'?(yes/no)")
         confirm = input().upper()
    os.system("sudo groupadd " + groupname)
    print('group added')
         

def remove_user():
    confirm = "N"
    while confirm != "Y":
        username=input("Enter the name of the user to remove: ")
        print("Remove the user: '"+username+"'?(y/n)")
        confirm = input().upper()
    os.system("sudo userdel -r "+username)
    print('user removed')

def add_user(): 
    confirm = "N"
    while confirm != "Y":
         username = input("enter the name of the user to add: ")
         print("use the user name '"+ username +"'?(y/n)")
         confirm = input().upper()
    os.system("sudo useradd " + username )
    print('user added')
    


x='0'
   
while x != '6':
    print('Plz choose a number')
    x=input('1-add user\n2-remove user\n3-add group\n4-add user to group\n5-show groups and users\n6-exit\n')

    if x=='1' :
        add_user()
    elif x=='2' :
        remove_user()
    elif x=='3' :
        add_group()
    elif x=='4' :
        add_user_to_group()
    elif x=='5' :
        show_group_users()
    else :
        print('exiting..')
        
         