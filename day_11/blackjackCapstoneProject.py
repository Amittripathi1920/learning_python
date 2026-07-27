import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

computer_cards = []
user_cards = []

computer_cards.append(random.choice(cards))
computer_cards.append(random.choice(cards))
print(f"Computer's first card: {computer_cards}")
