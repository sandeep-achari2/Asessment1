import random

def generate_random():
    random_number = random.randint(1, 100)
    attempts=0
    while True:
        user_input=int(input("Enter a number:"))
        attempts+=1
        if user_input<1 or user_input>100:
            print("Enter number between 1 to 100")
        elif user_input<random_number:
            print("Too Low")
        elif user_input>random_number:
            print("Too High")
        else:
            print(f'correct guess at {attempts} attempts')
            break

def main():
    generate_random()

main()
    