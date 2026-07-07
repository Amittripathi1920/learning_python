print("Welcome to the Rollercoaster!")

height = int(input("ENter your height in CM : "))
minor_age_ticket_price = "7$"
major_age_ticket_price = "12$"
children_ticket_price = "5$"
minor_age = 18
children = 12


if height >= 120:
    print("You can ride the RollerCoaster!")
    age = int(input("Please Enter your Age : "))


    if age <= children:
        print(f"Please pay {children_ticket_price} at the counter")
    elif age <= minor_age :
        print(f"Please pay {minor_age_ticket_price} at the counter")
    else:
        print(f"please pay {major_age_ticket_price} at the ticket counter")
else:
    print("Sorry you have to groww before you can ride :)")