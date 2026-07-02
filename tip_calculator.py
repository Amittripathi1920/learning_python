print("Welcome to the tip calculator")


bill = float(input("what was the total bill? :"))
tip = int(input("What percentage tip would you like to give? 5, 10, 13 : "))

total_bill = round(bill+(bill/100)*tip,2)
people = float(input("How many people to split the bill ? : "))

print(f"Each person should pay : {round((total_bill/people),2)}$")
