from data import question_data
from trivia_data import trivia_questions

class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

class QuestionData:
    def __init__(self):
        self.data = []
        for question in question_data:
            self.data.append(Question(question["text"], question["answer"]))
            
    def get_questions(self):
        for q in self.data:
            print(q.text)
            print(q.answer)

class TriviaQuestions:
    def __init__(self):
        self.trivia_data = []
        for question in trivia_questions:
            self.trivia_data.append(Question(question["question"], question["correct_answer"]))
    
    def get_trivia_questions(self):
        for q in self.trivia_data:
            print(q.question)
            print(q.correct_answer)
