
def loan_eligibility(salary,age,credit):
    if salary>=20000 and age>21 and credit>1000:
        print("Loan is approved because salary and credit score is good enough")
    else:
        print("Loan is rejected due to low salary or credit score")
    
def main():
    salary=int(input("Enter salary: "))
    age=int(input("Enter age: "))
    credit=int(input("Enter credit score: "))
    loan_eligibility(salary,age,credit)
    
main()