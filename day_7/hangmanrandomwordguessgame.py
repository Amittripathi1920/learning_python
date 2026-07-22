import random

words = [
    "apple", "banana", "orange", "grape", "mango",
    "table", "chair", "window", "door", "floor",
    "river", "mountain", "ocean", "forest", "desert",
    "happy", "sad", "quick", "slow", "bright",
    "computer", "keyboard", "screen", "mouse", "printer",
    "python", "program", "data", "logic", "function",
    "city", "village", "country", "road", "bridge",
    "music", "movie", "story", "book", "poem",
    "sun", "moon", "star", "cloud", "rain"
]

rand_word = random.choice(words)
len_rand_word = len(rand_word)
attempt = 0
placeholder_list = list("_" * len_rand_word)
print(rand_word)
placeholder = ""
print(placeholder)


while attempt <= len_rand_word:
    user_guess = input("Guess a letter : ").lower()
    if len(user_guess) < 2:
        if user_guess in rand_word:
            print(f"Correct Guess - Attempts Left - {len_rand_word - attempt}/{len_rand_word}")
            for i, ch in enumerate(rand_word):
                if ch == user_guess:
                    placeholder_list[i] = user_guess
            # print(user_guess)
            # print(placeholder_list)
            placeholder = "".join(placeholder_list)
            print(placeholder)
            if "_" not in placeholder_list:
                print("**********************************Congratulations! You Won**********************************")
                break
        else:
            attempt += 1

            print(f"-------------\nIncorrect Guess - Attempts Left - {len_rand_word - attempt}/{len_rand_word}")
            print(placeholder)
            if attempt == len_rand_word:
                print(f"**********************************YOU LOST BUDDY- Correct Word was - {rand_word}**********************************")
                break
    else:
        print("Choose only one letter at a time.....")

    
    
