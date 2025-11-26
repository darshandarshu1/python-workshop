def userInput():
    first_input=int(input("enter first number:"))
    second_input = int(input("enter second number:"))
    return first_input,second_input
def add(a=0,b=0):#if user not give take default 0
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
print("welcome to calculater")
while True:
    print("select the choose:\n 1.add \n 2.sub \n 3.mul \n 4.div \n 5.stop")
    choice=int(input("enter the choice:"))
    if choice==1:
        x,y=userInput()
        add(x,y)
        print("addiition of numbers is:",add(x,y))
    elif choice==2:
        x,y=userInput()
        sub(x,y)
        print("substraction of numbers is:",sub(x,y))
    elif choice==3:
        x,y=userInput()
        mul(x,y)
        print("multiplication of numbers is:",  mul(x,y))
    elif choice==4:
        x,y=userInput()
        div(x,y)
        print("division of numbers is:",div(x,y) )
    elif choice==5:
        break
    else:
        print("wrong input")


