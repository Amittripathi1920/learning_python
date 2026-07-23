def calculate_love_score(x,y):
    true_str = "true"
    l_str = "love"
    word = (x+y).lower()
    tr_count = 0
    l_count = 0

    for i in true_str:
        for j in word:
            if i == j:
                tr_count += 1

    for i in l_str:
        for j in word:
            if i == j:
                l_count += 1

    print(f"{tr_count}{l_count}")

calculate_love_score("Kanye West","Kim Kardashian")
