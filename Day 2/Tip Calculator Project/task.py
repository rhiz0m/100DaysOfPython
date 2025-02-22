# Boss challenge day 2.

#124.56
# 10 , 12, 15
# 12
# people 7
# total 19.93 each

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip_amount = bill * (tip / 100)
print(tip_amount)

total_price = bill + tip_amount
print(total_price)

split_bill = round(total_price / people, 2)

print(f"${split_bill}")