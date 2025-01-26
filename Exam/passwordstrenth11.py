
def strenth_checker(password):
    if len(password)<8:
        return "Weak passsword"
    else:
        any(c.isupper() for c in password)
        any(c.islower() for c in password)  
        any(c.isdigit() for c in password)
        any(not c.isalnum() for c in password)
        return "Strong password"
    
def main():
    password = input("Enter password: ")
    print(strenth_checker(password))
    
main()