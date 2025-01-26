
def factorial(n):
    if n<0:
        return "Error input and negative number"
    elif n==0:
        return 1
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact

def main():
    n=int(input("enter a number:"))
    print(f'factorial of {n} is {factorial(n)}')
    
main()

        