
def string_analysis(input_string):
    vowels="aeiouAEIOU"
    digits="0123456789"
    vowels_count=0
    consonant_count=0
    digit_count=0
    specialchar_count=0
    
    string=" "
    for i in input_string:
        if i in vowels:
            vowels_count+=1
        elif i in digits:
            digit_count+=1
        elif i.isalpha():
            consonant_count+=1
        else:
            specialchar_count+=1
        
    return vowels_count,consonant_count,digit_count,specialchar_count
    

def main():
    input_string=input("enter string:")
    (vowels_count,consonant_count,digit_count,specialchar_count)=string_analysis(input_string)
    print(f'vowels count:{vowels_count}')
    print(f'consonant count:{consonant_count}')
    print(f'digit count:{digit_count}')
    print(f'special character count:{specialchar_count}')
    
main()