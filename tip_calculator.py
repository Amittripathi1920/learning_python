print("Welcome to the tip calculator")


bill = float(input("what was the total bill? :"))
tip = float(input("How much tip would you like to give? 5, 10, 13 : "))

total_bill = bill+tip
people = float(input("How many people to split the bill ? : "))

print(f"Each person should pay : {round((total_bill/people),2)}")
