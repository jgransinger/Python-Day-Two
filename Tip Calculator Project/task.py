from os.path import split

print("Welcome to the tip calculator! ")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15: "))
people = int(input("How many people to split the bill?: "))

total_after_tip = bill * (1 + (tip * 0.01))
split_total = total_after_tip / people
split_total_rounded = round(split_total, 2)
print(f"Each person should pay: ${split_total_rounded:.2f}")