import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

users_choice = input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors!\n")
game_items = [rock, paper, scissors]
computers_choice = random.choice(game_items)

result = ""

if users_choice == "0":
    users_choice = rock

    if users_choice == computers_choice:
        result = "Its a draw..."
    elif computers_choice == paper:
        result = "You loose..."
    elif computers_choice == scissors:
        result = "You win!"

elif users_choice == "1":
    users_choice = paper

    if users_choice == computers_choice:
        result = "Its a draw..."
    elif computers_choice == scissors:
        result = "You loose..."
    elif computers_choice == rock:
        result = "You win!"

elif users_choice == "2":
    users_choice = scissors

    if users_choice == computers_choice:
        result = "Its a draw..."
    elif computers_choice == rock:
        result = "You loose"
    elif computers_choice == paper:
        result = "You win!"
else:
    result = "Sorry, not a valid number"

print("Your choice:")
print(users_choice)
print("Computers choice:")
print(computers_choice)
print(result)