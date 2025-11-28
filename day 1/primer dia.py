print("welcome to my restaurant")
bill = float(input("What was the total bill? > "))
tip = int(input("What percentage tip would you like to give? 10,12 or 15? > "))
people_split = int(input("How many people to split the bill? > "))

tip_percent = tip / 100
total = bill * tip_percent
total_bill = bill + total
bill_per_person = total_bill / people_split
print(f"Each person should pay: $ {round(bill_per_person,2)} ")
