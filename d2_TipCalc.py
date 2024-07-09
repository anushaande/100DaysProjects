print("Welcome to the tip calculator!")
bill = float(input("What is the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

pay = (((tip * bill)/100) + bill) / people
# bill_per_person = round(pay,2)

bill_per_person = "{:.2f}".format(pay)

print(f"Each person should pay: ${bill_per_person}")