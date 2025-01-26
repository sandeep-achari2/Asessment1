
def Multiplication_table(number,start,end):
    for i in range(start,end+1):
        print(f'{number}*{i}={number*i}')
        
def main():
    number=int(input("enter Multiplication table number: "))
    start=int(input("enter start val: "))
    end=int(input("enter end val:"))
    Multiplication_table(number,start,end)
main()