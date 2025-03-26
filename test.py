import random
x = int(input("Enter a number: "))

y = random.randint(1, 100)

cont = True

while (cont):
    x = int(input("Enter a number: "))
    if x > y:
        print("Too high")
    elif x < y:
        print("Too low")
    else:
        print("Correct!")
        cont = False
