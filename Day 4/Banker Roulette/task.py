import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

random_friend_option1 = random.choice(friends)
print(random_friend_option1)

random_friend_option2 = random.randint(0, 4)

print(friends[random_friend_option2])