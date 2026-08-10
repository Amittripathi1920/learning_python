"""Program Requirements
1. Print Report
2. Check Resources sufficient?
3. Process Coins
4. Check Transaction successful
5. Make Coffee
"""

menu = {
    "espresso": {
        "ingrediants" : {
            "water" : 50,
            "coffee" : 18,
        },
        "cost" : 1.5
    },
    "latte" : {
        "ingrediants" : {
            "water" : 200,
            "milk" : 150,
            "coffee" : 24,
        },
        "cost" : 2.5
    },
    "cappuccino" : {
        "ingrediants" : {
            "water" : 250,
            "milk" : 100,
            "coffee" : 24,
        },
        "cost" : 3.0,
    }
}

resources = {
    "water" : 300,
    "milk" : 200,
    "coffee" : 100,
}

money = 0
turn_on = True

print('''Welcome to Coffee Machine ☕''')

def report():
    print("Below resources are available: ")
    resources_with_money = resources
    resources_with_money["Money"] = money
    for i in resources:
        print(f'''{i} : {resources[i]}''')

def resource_check(u_choice):
    if u_choice in ["cappuccino", "latte", "espresso"]:
        item_sufficiency = []
        selected_menu = menu[u_choice]["ingrediants"]
        for i in selected_menu:
            if selected_menu[i] <= resources[i]:
                item_sufficiency.append("sufficient")
                # print(f"{i} : Sufficient")
            else:
                item_sufficiency.append("not sufficient")
                print(f"Sorry there is not enough {i}.")
        if "not sufficient" in item_sufficiency:
            return False
        else:
            return True
        print(selected_menu)
        print(item_sufficiency)

def process_coin(quarter, dime, nickle, penny):
    return quarter * 0.25 + dime * 0.1 + nickle * 0.05 + penny * 0.01 

# def substract_resource(u_choice):
#     if u_choice in ["cappuccino", "latte", "espresso"]:
#         updated_resources = {}
        
#         for i in resources:
#             if menu[u_choice]["ingrediants"][i] in resources:
#                 updated_resources[i] = resources[i] - menu[u_choice]["ingrediants"][i]
#         print(updated_resources)

def substract_resource(u_choice):
    if u_choice in ["cappuccino", "latte", "espresso"]:

        for item in menu[u_choice]["ingrediants"]:
            resources[item] -= menu[u_choice]["ingrediants"][item]

        # print("Resources updated:", resources)

while turn_on:
    u_choice = input('''What would you like? Type A,B,C or D to choose.
    A: espresso
    B: latte
    C: cappuccino
    D: Report
    ''').lower()
    selected_drink = ""
    if u_choice == "a":
        selected_drink = "espresso"
    elif u_choice == "b":
        selected_drink = "latte"
    elif u_choice == "c":
        selected_drink = "cappuccino"
    elif u_choice == "d":
        report()
    elif u_choice == "off":
        turn_on = False
        break
    else:
        print("Please choose correct option....")

    if resource_check(selected_drink):
        print("Please Insert Coin 💰")
        quarter = float(input("How many quarters? : "))
        dime = float(input("How many dimes? : "))
        nickle = float(input("How many nickles? : "))
        penny = float(input("How many pennies? : "))
        total = process_coin(quarter = quarter, dime = dime, nickle = nickle, penny = penny)
        selected_drink_cost = menu[selected_drink]["cost"]
        if total >= selected_drink_cost:
            print(f"Here is your {round((total - selected_drink_cost), 2)}$ change.\nEnjoy your {selected_drink}☕ ")
            money += menu[selected_drink]["cost"]
            report()
            substract_resource(selected_drink)
        else:
            print(f"Sorry that's not enough money. money refunded\n{selected_drink} cost: {selected_drink_cost}$ and you gave: {total}$")


    # else:
    #     print("☕")


