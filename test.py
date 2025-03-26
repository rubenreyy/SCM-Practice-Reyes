import random
x = input("Enter a number: ")

y = random.randint(1, 10)
if x == y:
    print("You win!")
else:
    print("You lose!")