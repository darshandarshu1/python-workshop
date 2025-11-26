def election(age):
    if age>18:
        print("you are eligible to vote")
    else:
        print("not eligible")
age=int(input("enter you age:"))
election(age)