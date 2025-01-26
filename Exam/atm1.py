
def simulation(balance):
    return balance

def deposit_money(balance,amount):
    if amount>0:
        balance+=amount
        print(f'amount deposited:{amount}')
    else:
        print("Invalid amount")
    return balance

def withdraw_money(balance,amount):
    if amount<=0:
        print("invalid amount")
    elif amount>balance:
        print("Insufficient balance")
    else:
        balance-=amount
        print(f'Amount withdraw: {amount}')
        print(f'Remaining balance:{balance}')
    return balance
    

def main():
    balance=1000
    while True:
        print("1.Deposit")
        print("2.Withdraw")
        print("3.Balance")
        print("4.Exit")
        choice=int(input("enter Choice:"))
        
        if choice==1:
            amount=int(input("Enter amount: "))
            balance=deposit_money(balance,amount)
        elif choice==2:
            amount=int(input("Enter amount: "))
            balance=withdraw_money(balance,amount)
            break
        elif choice==3:
            print(f'Balance:{balance}')  
            break
        else:
            print("Invalid choice")
main()
        