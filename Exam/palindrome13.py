
def palindrome(str):
    n=len(str)
    for i in range(n//2):
        if str[i]!=str[n-i-1]:
            return False
    return True

def main():
    str = input("Enter a string: ")
    if palindrome(str):
        print("Palindrome")
    else:
        print("Not Palindrome")
        
main()