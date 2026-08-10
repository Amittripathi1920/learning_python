
enemies = 1

def increase_enemies():
    enemies = 4
    print(f"Inside - {enemies}")

increase_enemies()
print(f"Outside : {enemies}")

def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True

u_input = int(input("Enter a number to check : "))

# Test
print(f"{u_input} - {is_prime(u_input)}")   # True
# print(is_prime(10))  # False



def is_leap(year):
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

    # Target is the number up to which we count
def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        if number % 3 == 0:
            print("Fizz")
        if number % 5 == 0:
            print("Buzz")
        else:
            print(number)
