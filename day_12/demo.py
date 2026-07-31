
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