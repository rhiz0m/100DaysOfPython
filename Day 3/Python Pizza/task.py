print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
bill = 0

if size == "S":
    bill += 15

elif size == "M":
    bill += 20

elif size == "L":
    bill += 25

pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")

# $2 for size S , $3 for size M & L
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

extra_cheese = input("Do you want extra cheese? Y or N: ")

if extra_cheese == "Y":
    bill += 1
print(f"Your final bill is: ${bill}.")