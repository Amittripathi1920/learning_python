import random

continue_game = True

def numberCheck(random_digit : int, u_input: int, max_attempts:int):
    # global max_attempts
    max_attempts = max_attempts
    if random_digit < u_input:
        max_attempts -= 1
        return "Too High" 
    elif random_digit > u_input:
        max_attempts -= 1
        return "Too Low"
    else :
        return "You Got it!"

while continue_game:

    difficulty_level = input("Choose a difficulty level (E = easy, M = medium, H = hard): ").lower()

    if difficulty_level == "e":
        max_attempts = 10
    elif difficulty_level == "m":
        max_attempts = 7
    elif difficulty_level == "h":
        max_attempts = 5
    else :
        print("Invalid Level selected, please Choose correct difficulty level (E = easy, M = medium, H = hard): ")
        continue_game = False
        break

    
    random_digit = random.randint(1,100)
    for i in range(max_attempts):
        print(f"You have {max_attempts} attempts remaining to guess the number")
        u_input = int(input("Make a Guess: "))
        # x = numberCheck(random_digit=random_digit, u_input=u_input, max_attempts=max_attempts)
        # print(random_digit)
        if random_digit < u_input:
            max_attempts -= 1
            print("Too High") 
        elif random_digit > u_input:
            max_attempts -= 1
            print( "Too Low")
        else:
            print( "You Got it! Congratulations Winner")  
            break

        if max_attempts == 1:
            print("This is your last guess, Think Before Typing.................")
        elif max_attempts == 0 and u_input != random_digit:
            print("You Lost\nThank You")
        # print(f"u_input: {u_input},\nAttempts Left: {max_attempts}\nCorrect Ans: {random_digit}")
    u_choice = input("Would You Like to play again? Type [Y/N] only: ").lower()
    if u_choice != 'y':
        print("Thank You for Playing....")
        continue_game = False
    else:
        print( '\n' * 20)


