higher_lower_qna = [
    {
        "question": "Which is higher?",
        "option_a": "Mount Everest",
        "option_b": "K2",
        "answer": "Mount Everest"
    },
    {
        "question": "Which has more population?",
        "option_a": "India",
        "option_b": "USA",
        "answer": "India"
    },
    {
        "question": "Which is larger?",
        "option_a": "Pacific Ocean",
        "option_b": "Atlantic Ocean",
        "answer": "Pacific Ocean"
    },
    {
        "question": "Which country is bigger in area?",
        "option_a": "Canada",
        "option_b": "China",
        "answer": "Canada"
    },
    {
        "question": "Which has more users?",
        "option_a": "Instagram",
        "option_b": "Twitter (X)",
        "answer": "Instagram"
    },
    {
        "question": "Which river is longer?",
        "option_a": "Nile",
        "option_b": "Amazon",
        "answer": "Nile"
    },
    {
        "question": "Which desert is larger?",
        "option_a": "Sahara",
        "option_b": "Arabian Desert",
        "answer": "Sahara"
    },
    {
        "question": "Which city is more populated?",
        "option_a": "Tokyo",
        "option_b": "New York City",
        "answer": "Tokyo"
    },
    {
        "question": "Which country has more islands?",
        "option_a": "Indonesia",
        "option_b": "Philippines",
        "answer": "Indonesia"
    },
    {
        "question": "Which is colder?",
        "option_a": "Antarctica",
        "option_b": "Arctic",
        "answer": "Antarctica"
    }
]

options = [{"a": "option_a"},
           {"b": "option_b"}]

continue_game = True
score = 0


for i in higher_lower_qna:
    print(f"{i["question"]} \nA: {i["option_a"]} B: {i['option_b']}")
    u_choice = input("Please select option A or B : ").lower()
    if u_choice in ["a","b"]:
        if u_choice == "a":
            selected = i["option_a"]
        else:
            selected = i["option_b"]
        if selected == i["answer"]:
            score += 1
            print(f"Your Total Score: {score}")
        else:
            
            print(f"Your Total Score: {score}")
            break
    else:
        print("Please select valid option")
        print(f"Your Total Score: {score}")
        break
        