print("Welcome to the Rollercoaster!")

height = int(input("ENter your height in CM : "))
minor_age_ticket_price = 7
major_age_ticket_price = 12
children_ticket_price = 5
minor_age = 18
children = 12
photo_price = 3
bill = 0


if height >= 120:
    print("You can ride the RollerCoaster!")
    age = int(input("Please Enter your Age : "))


    if age <= children:
        print(f"Child tickets are ${children_ticket_price}")
        bill = children_ticket_price
    elif age <= minor_age :
        bill = minor_age_ticket_price
        print(f"Youth tickets are ${minor_age_ticket_price}")
    else:
        bill = major_age_ticket_price
        print(f"Adults tickets are ${major_age_ticket_price}")

    photo = input("Do You want to have photo take? type y for Yes and n for No.")
    if photo == "y" :
        bill += photo_price
    print(f"Your Total Bill = ${bill}")

else:
    print("Sorry you have to groww before you can ride :)")