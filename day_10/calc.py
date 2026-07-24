def add(x,y):
    return x + y

def substract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def devide(x, y):
    return x / y

# while should_continue:
#     f_number = float(input("What"s the First Number? : "))
#     list_of_operations = ["+", "-", "*", "/"]
#     for item in list_of_operations:
#         print(f"     {item}")
#     operation = input("What Operation would you like to Perform? : ")
#     if operation not in list_of_operations:
#         print("Please Choose Valid Options available.")
#         should_continue = False
#         break
#     else:
#         pass
#     s_number = float(input("What"s the second Number? : "))
    
#     if operation == "+":
#         result = add(f_number, s_number)
#     elif operation == "-":
#         result = substract(f_number, s_number)
#     elif operation == "*":
#         result = multiply(f_number, s_number)
#     elif operation == "/":
#         result = devide(f_number, s_number)
#     else:
#         print("NA")
#     print(f"Answer : {result}")
#     should_repeat = input(f"Type Y to continue calculating with {result}, or N to start a new calculation? : ").lower()
#     # if should_repeat == "y":

# ------------------------------------------------------------------------------

operations = {
    "+" : add,
    "-" : substract,
    "*" : multiply,
    "/" : devide
}

def calculator():

    f_number = float(input("What's the First Number? : "))
    should_continue = True
    while should_continue:
        
        # list_of_operations = ["+", "-", "*", "/"]
        for item in operations:
            print(f"     {item}")
        operation = input("What Operation would you like to Perform? : ")
        if operation not in operations:
            print("Please Choose Valid Options available.")
            should_continue = False
            break
        else:
            pass
        s_number = float(input("What's the second Number? : "))

        for i in operations:
            # print(f"Operation : {i}")
            if operation == i:
                result = operations[i](f_number,s_number)
                print(f"{f_number} {operation} {s_number} = {result}")

        should_repeat = input(f"Type Y to continue calculating with {result}, or N to start a new calculation? : ").lower()
        if should_repeat == "y":
            f_number = result
        else:   
            should_continue = False
            print("Starting a new calculation...") 
            calculator()

calculator()
    





        