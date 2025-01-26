
def add_items(cart_item):
    name=input("Enter item name: ")
    price=int(input("Enter price: "))
    cart_item.append({'name':name,'price':price})
    
def view_cart_items(cart_item):
    for item in cart_item:
        print(f'{item["name"]} : {item["price"]}')
    
def calculate_total(cart_item):
    total=0
    for item in cart_item:
        total+=item['price']
    print(f'Total price is: {total}')
    
def main():
    cart_item=[]
    while True:
        print("1. Add item")
        print("2. View cart items")
        print("3. Calculate total")
        print("4. Exit")
        choice=int(input("Enter your choice: "))
        if choice==1:
            add_items(cart_item)
        elif choice==2:
            view_cart_items(cart_item)
        elif choice==3:
            calculate_total(cart_item)
            break
        elif choice==4:
            break
        else:
            print("Invalid choice")
    
main()
    