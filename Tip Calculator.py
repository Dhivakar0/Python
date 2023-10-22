print("Welcome to the tip calculator.")
bill = float(input("What was the total bill in $?\n"))
tip_percentage = int(input("Enter the tip percentage (e.g. 5, 7, 10): "))
split = int(input("How many people are splitting the bill?\n"))
tip = tip_percentage / 100
tip_amount = bill * tip
amount = bill + tip_amount
pay = round((amount / split), 2)

print(f"Each person should pay ${pay:.2f}")

