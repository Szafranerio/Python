#Constructor __init__(self)
class User():
    def __init__(self, user_id, username, user_age, user_sex):
        self.id = user_id
        self.name = username
        self.age = user_age
        self.sex = user_sex
        self.followers = 0
        self.following = 0
    
    def follow(self, user):
        user.followers += 1
        self.following += 1
    
user_1 = User('001', 'Szafranerio', 24, 'Male')
user_2 = User('002', 'Angela', 24, 'Female')


user_1.follow(user_2)

print(f'You are {user_1.name}, your id is {user_1.id} You are allowed to drink, because you are {user_1.age}. You are {user_1.sex}, and you are following {user_1.following} users')

#OOP Project: Quize Game, rest of the code in the separte folder called "OOP"

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question["text"]
    questions_answer = question['answer']
    new_question = Question(text=question_text, answer=questions_answer)
    question_bank.append(new_question)
    
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

quiz.stop_game()
     
print('You are done')
print(f'Your final score is: {quiz.score}/ len{question_bank}') 



