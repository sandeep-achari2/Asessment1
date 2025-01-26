
def is_prime(n): #checking for prime or not
    if n<2:
        return False
    if n==2:
        return True
    for i in range(2,n):
        if n%i==0:
            return False
        return True
    
def print_range_prime(start,end):      #function to print prime numbers in given range  
    print(f'prime number range from {start} to {end} is:')
    for i in range(start,end+1): # for loop to check prime numbers
        if is_prime(i):
            print(i)
    print()

def main(): #main function calling the function
    start=int(input("Enter starting number: "))
    end=int(input("Enter ending number: "))
    print_range_prime(start,end)

main()