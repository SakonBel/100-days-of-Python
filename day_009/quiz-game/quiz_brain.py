class QuizBrain:
    def __init__(self, q_list):
        self.score = 0
        self.question_number = 0
        self.question_list = q_list

    def still_has_question(self):
        return len(self.question_list) > self.question_number

    def next_question(self):
        answer = input(
            f"Q.{self.question_number+1} : {self.question_list[self.question_number].text} (True or False) : ")
        self.check_answer(
            answer, self.question_list[self.question_number].answer)
        print(f"Your score is : {self.score}/{self.question_number + 1}\n")
        self.question_number += 1

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}")
