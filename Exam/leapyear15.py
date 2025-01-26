
def leap_year_check(year):
    if year%4==0:
        if year%100!=0 or year%400==0:
            return True
        else:
            return False
            
def main():
    iterations=int(input("Enter number of iterations: "))
    for i in range(iterations):
        year=int(input("Enter year: "))
        if leap_year_check(year):
            print("Leap year")
        else:
            print("Not a leap year")

main()
    