from question_model import QuestionData, TriviaQuestions

class QuizBrain:
    def __init__(self):
        self.qd = QuestionData()
        self.tq = TriviaQuestions()
        self.q_no = 0
        self.score = 0
        self.wrong_answers = 0
        self.quiz_on = True

    def quiz(self):
        while (self.quiz_on):    
            answer = input(f"\nQ.{self.q_no}: {self.qd.data[self.q_no].text} (True/False)?: ")
            if answer == self.qd.data[self.q_no].answer:
                print("You got it right")
                self.score += 1
            else:
                print("That's the Wrong Answer")
                self.wrong_answers += 1 
            if self.wrong_answers >= 3:
                self.quiz_on = False 
            print(f"The correct answer was: {self.qd.data[self.q_no].answer}. \nYour current Score is {self.score}/{self.q_no + 1}")           
            if  (self.q_no >= len(self.qd.data) - 1):
                self.quiz_on = False
                print("\nQUIZ OVER!")
            self.q_no += 1
        return [self.score]
    

    def trivia_quiz(self):
        while (self.quiz_on):    
            answer = input(f"\nQ.{self.q_no}: {self.tq.trivia_data[self.q_no].text} (True/False)?: ")
            if answer == self.tq.trivia_data[self.q_no].answer:
                print("You got it right")
                self.score += 1
            else:
                print("That's the Wrong Answer")
                self.wrong_answers += 1 
            if self.wrong_answers >= 3:
                self.quiz_on = False 
            print(f"The correct answer was: {self.tq.trivia_data[self.q_no].answer}. \nYour current Score is {self.score}/{self.q_no + 1}")           
            if  (self.q_no >= len(self.tq.trivia_data) - 1):
                self.quiz_on = False
                print("\nQUIZ OVER!")
            self.q_no += 1
        return [self.score]

    



