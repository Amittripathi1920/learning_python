import random

def card_total(x:list):
    total_val = 0
    for i in x:
        total_val += i
    return total_val

def blackjack_check(x:list):
    if 11 in x and 10 in x:
        return True
    else :
        return False

def ace_check(a: list):
    if 11 in a:
        return True
    else :
        return False

def total_check(x:int):
    if x < 21:
        return True
    else:
        return False

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

computer_cards = []
user_cards = []
computer_cards.extend(random.sample(cards, 2))
user_cards.extend(random.sample(cards, 2))

while_loop = True
# computer_cards = [10,11]
# user_cards = [11,10]
while while_loop:
    print(f"Computer's Cards: {computer_cards}")
    print(f"User's Card: {user_cards}")
    print(f"Computer's Total: {card_total(computer_cards)}")
    print(f"User's Total: {card_total(user_cards)}")

    isComputerBlackJack = blackjack_check(computer_cards)
    isUserBlackJack = blackjack_check(user_cards)

    print("------------------------------BlackJack Check---------------------------------------")
    print(f"Computer BlackJack: {isComputerBlackJack}\nUser BlackJack: {isUserBlackJack}")

    if isComputerBlackJack != isUserBlackJack:
        if isUserBlackJack:
            print(f"------------------Congratulations! User Won. User Has BlackJack------------------------------")
        elif isComputerBlackJack:
            print(f"------------------Congratulations! Computer Won. Computer Has BlackJack------------------------------")
    elif isComputerBlackJack == True and isUserBlackJack == True:
        print("------------------It's Draw------------------")
    else:
        if total_check(card_total(computer_cards)):
            u_choice = input("Do you want to draw another card? Type [Y/N] : ").strip().lower()
            if u_choice == 'y':
                computer_cards.extend(random.sample(cards, 1))
                user_cards.extend(random.sample(cards, 1))
            else:
                while_loop = False
        else:
            if ace_check(computer_cards):
                updated_total = card_total - 10
                if updated_total > 21:
                    print("You Loose")
                    while_loop = False
                else:
                    u_choice = input("Do you want to draw another cards? Type [Y/N] : ").strip().lower()
                    if u_choice == 'y':
                        computer_cards.extend(random.sample(cards, 1))
                        user_cards.extend(random.sample(cards, 1))
                    else:
                        print("You have not selected Anything")
                        while_loop = False                
            else :
                print("You Lost")
                while_loop = False
    
            
    print(ace_check(computer_cards))
