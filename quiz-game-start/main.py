from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for q in question_data:
    question_text = q["text"]
    question_answer = q["answer"]
    question = Question(question_text, question_answer)
    question_bank.append(question)


quiz = QuizBrain(question_bank)
quiz.end_quiz()








"""
import random
question_for_user = random.choice(question_bank)
question_text = question_for_user.question
user_answer = input(question_text).title()
print (user_answer, question_for_user.answer)
if user_answer == question_for_user.answer:
    print("You got it right")
else:
    print("sorry, you are wrong")
"""