import random
x = input("Enter a number: ")

y = random.randint(1, 100)
if x == y:
    print("You win!")
else:
    print("You lose!")