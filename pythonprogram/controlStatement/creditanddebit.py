balance=10000
while True:
    type=input("credit or debit:")
    if(type=="stop"):
        break
    elif(type=="debit"):
        debit=int(input("enter amount:"))
        if(debit>10000):
            print("balance is not suffient")
        else:
            balance=balance-debit
            print(debit,"amount debited successfull")
            print("remaining balance",balance)

    elif(type=="credit"):
        credit=int(input("enter amount for credit"))
        balance+=credit
        print("your new balance",balance)
    else:
        print(balance)
