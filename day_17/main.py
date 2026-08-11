from question_model import Question
from data import question_data
from quiz_brain import QuizBrain



question_bank = []

for i in question_data:
    new_question = Question(i["text"], i["answer"])
    question_bank.append(new_question)

# print(question_bank[1].text)

quiz = QuizBrain(question_list=question_bank)
# quiz.current_question()

while quiz.still_has_question():
    quiz.next_question()


print(f"------------------You have completed the quiz--------------\n--- Your Final Score Was: {quiz.score}/{quiz.question_number}")
