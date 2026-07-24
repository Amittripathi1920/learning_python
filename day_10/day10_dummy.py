# def format_name(f_name, l_name):
#     result = (f_name + ' ' + l_name).title()
#     return result

# f_name = input("What's your First name: ")
# l_name = input("what's your Last name: ")

# formatted_str = format_name(f_name, l_name)
# print(formatted_str)

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

print(is_leap_year(2100))