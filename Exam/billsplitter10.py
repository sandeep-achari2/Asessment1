
def bill_splitter(total_bill,n,tip_percent):
    tip_amount=(total_bill*tip_percent)//100
    total_bill+=tip_amount
    per_person_bill=total_bill/n
    return per_person_bill
    
def main():
    total_bill=float(input("Enter total bill amount: "))
    n=int(input("Enter number of people: "))
    tip_percent=float(input("Enter tip percent: "))
    print(f'Each person should pay {bill_splitter(total_bill,n,tip_percent)}')
    
main()