print("Welcome to the Tip Calculator ")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
total_bill = tip/100 * bill + bill
split_bill_per_person = total_bill/people
final_amount = round(split_bill_per_person, 2)
print(f"Each person should pay ${final_amount}")