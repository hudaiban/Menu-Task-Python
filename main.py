def addUser():
    print("\nUser added!!\n")


def deleteUser():
    print("\nuser deleted!!\n")


def addGroup():
    print("\nGroup added!!\n")


def removeGroup():
    print("\nGroup removed\n")


def showGroup():
    print("\nGroup users:\n"
          "\n1"
          "\n2"
          "\n3"
          )
i = 1
while(i >= 1):
    print("1-Add User \n"
          "2-Remove User \n"
          "3-Add Group\n"
          "4-Remove Group\n"
          "5-Show Group & Users\n"
          "-1 to exit\n")
    i =int( input("please select a specific task: "))
    if(i == 1):
        addUser()
    elif(i == 2):
        deleteUser()
    elif(i == 3):
        addGroup()
    elif(i == 4):
        removeGroup()
    elif(i == 5):
        showGroup()

    elif (i == -1):
        print("thank you")
    else:
        print("\nwrong input\n")