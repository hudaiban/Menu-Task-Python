print("enter a number")
x = input()
print(switch(x))

def switch(x):
  if x =="1":
    return "Add User"
  elif x=="2":
    return "remove user"
  elif x=="3":
    return "Add Group"
  elif x=="4":
     return "Remove group"
  elif x=="5":
     return "Show Group & Users"
