user_name=input("enter username:")
if((user_name=="Darshan")|(user_name=="Dhanu")):
    print("valid user")
    password=input("enter a password:")
    if(password=="user@123"):
        print("valid")
    else:
        print("not valid")
else:
    print("not a valid user")
