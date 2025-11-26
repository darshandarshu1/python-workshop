balance=10000
amount=int(input("enter amount:"))
if(amount>10000):
    print("balance is not suffient")
    print("if yo an to credit?if yes enter amount")
else:
    balance=balance-amount
    print(amount,"amount debited successfull")
    print("remaining balance",balance)