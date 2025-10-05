class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        question_for_user = self.question_list[self.question_number]
        self.question_number += 1

        #retrieve the question and the answer at the qestion_number
        question_text = question_for_user.question
        correct_answer = question_for_user.answer

        # prompt the question to the user
        user_answer = input(f"Q{self.question_number}. {question_text}").title()

        # check answers and track user's score
        self.check_answer(user_answer, correct_answer)



    def check_answer(self, user_answer, correct_answer):
        """check answers if correct and return a bool"""
        if user_answer == correct_answer:
            self.score += 1
            print("you got it right")
            return True
        else:
            print("you are wrong")
            return False


    def end_quiz(self):
        while self.question_number < len(self.question_list):
            self.next_question()
        print (f"The quiz is ended. Your final score is {self.score}/{len(self.question_list)}")


    def still_has_question(self):
        return self.question_number < len(self.question_list)
