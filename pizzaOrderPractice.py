print("Hi, Welcome to Dominos.\n==================================")

#Pizza Prices

small_pizza = 15
medium_pizza = 20
large_pizza = 25

#Pepperoni Prizes
pepperoni_small_pizza = 2
pepperoni_medium_pizza = 3

extra_cheese = 2

#Logic Code

i_size = input("What size pizza do you want? S, M or L : ")
i_pepperoni = input("Do you want Pepperoni? Y for YES and N for NO : ")
i_cheese = input("Do you want Extra Cheese? Y for YES and N for NO : ")

bill = 0
pepperoni = 0
if i_size.lower() == "s":
    bill += small_pizza
    if i_pepperoni.lower() == "y":
        bill += pepperoni_small_pizza
elif i_size.lower() == "m":
    bill += medium_pizza
    if i_pepperoni.lower() == "y":
        bill += pepperoni_medium_pizza
elif i_size.lower() == "l":
    bill += large_pizza
    if i_pepperoni.lower() == "y":
        bill += pepperoni_medium_pizza

if i_cheese.lower() == "y":
    bill += extra_cheese

if bill > 0 :
    print(f"Your Total Bill is : ${bill}\nThank You For Order\nSee You Soon :)")
else:
    print("Please choose correct size : S, M or L")