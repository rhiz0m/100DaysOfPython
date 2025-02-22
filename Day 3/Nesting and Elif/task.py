print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("How old are you?"))
    if age < 12:
        print("$5 please!")
    elif age <= 18:
        print("$7, please!")
    elif age > 18:
        print("12$, please!")
else:
    print("Sorry you have to grow taller before you can ride.")
