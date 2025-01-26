
def pattern(n):
    print("Ordered pattern")
    for i in range(n):
        for j in range(i+1):
            print('*',end='')
        print()

def reverse_pattern(n):
    print("Reverse pattern")    
    for i in range(n):
        for j in range(n-i):
            print('*',end='')
        print()

def main():
    n=int(input("Enter number: "))
    pattern(n)
    reverse_pattern(n)
    
main()