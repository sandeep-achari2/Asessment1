
def bm_calculator(weight,height):
    bmi=weight/(height**2)
    if bmi<18.5:
        return "Underweight"
    elif bmi<24.9:
        return "Normal"
    elif bmi<29.9:
        return "Overweight"
    else:
        return "Obese"
    
    
def main():
    weight=float(input("Enter weight in kg: "))
    height=float(input("Enter height in meters: "))
    print(bm_calculator(weight,height))

    
main()