
def conversions(): # type of conversions and select type of conversion
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    print("7. Exit")
    choice=int(input("Enter your choice: ")) 
    return choice

def celsius_to_fahrenheit(celsius):  #celsius to fahrenheit conversion
    fahrenheit=(celsius*9/5)+32      #formula
    return fahrenheit               #returning conversion 

def fahrenheit_to_celsius(fahrenheit): #fahrenheit to celsius conversion
    celsius=(fahrenheit-32)*5/9
    return celsius

def celsius_to_kelvin(celsius): #celsius to kelvin conversion
    kelvin=celsius+273
    return kelvin

def kelvin_to_celsius(kelvin):    #kelvin to celsius conversion
    celsius=kelvin-273
    return celsius

def fahrenheit_to_kelvin(fahreinheit):  #fahrenheit to kelvin conversion
    kelvin=(fahreinheit-32)*5/9+273
    return kelvin

def kelvin_to_fahrenheit(kelvin):   #kelvin to fahrenheit conversion
    fahrenheit=(kelvin-273)*9/5+32
    return fahrenheit

def main():
    while True:
        choice=conversions()  #select one type of conversion needed
        if choice==1:
            fahreinheit=float(input("Enter celsius:"))
            print("Temp in Fahrenheit is:",celsius_to_fahrenheit(fahreinheit)) #call the function and printing the value
        elif choice==2:
            celsius=float(input("Enter fahrenheit:"))
            print("Temp in Celsius is:",fahrenheit_to_celsius(celsius))#call the function and printing the value
        elif choice==3:
            kelvin=float(input("Enter celsius:"))
            print("Temp in Kelvin is:",celsius_to_kelvin(kelvin))#call the function and printing the value
        elif choice==4:
            celsius=float(input("Enter kelvin:"))
            print("Temp in Celsius is:",kelvin_to_celsius(kelvin))#call the function and printing the value
        elif choice==5:
            kelvin=float(input("Enter fahrenheit:"))
            print("Temp in Kelvin is:",fahrenheit_to_kelvin(kelvin))#call the function and printing the value
        elif choice==6:
            fahrenheit=float(input("Enter kelvin:"))
            print("Temp in Fahrenheit is:",kelvin_to_fahrenheit(fahrenheit))#call the function and printing the value
        elif choice==7:
            break
        else:
            print("Invalid choice")  #if we enter wrong choice print invalid

main()