print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("that will be $5.")
        bill += 5
    elif age <= 18:
        print("that will be $7.")
        bill += 7
    else:
        print("that will be $12.")
        bill += 12

    buy_photo = input("Do you want to buy a photo?")
    if buy_photo == "no":
        print("Ok, have a good day!")
    elif buy_photo == "yes":
        print("that will be $3!")
        bill += 3

    print(f"The total cost today will be ${bill}")
else:
    print("Sorry you have to grow taller before you can ride.")