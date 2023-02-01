print("Welcome to the Tip Calculator")

bill_amount = float(input("What was the total bill ? $"))

tip = int(input("What percentage tip would you like to give? 10,12 or 15?  "))
tip_amount = (bill_amount*tip)/100

total_bill = bill_amount + tip_amount

total_members = int(input("How many people to split the bill? "))

each_one_payment = round(total_bill/total_members, 2)

print(f"Each person should pay: ${each_one_payment}")