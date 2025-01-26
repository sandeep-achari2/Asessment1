
def odd_even_sep(list):
    odd=[]
    even=[]
    for i in list:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    return odd,even

def main():
    list=[1,2,3,4,5,6,7,8,9,10,85,75,89]
    print("Even and odd numbers are:",odd_even_sep(list))
    
main()