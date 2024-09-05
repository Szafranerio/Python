from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quiz Game")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_lavel = Label(text='Score: 0', bg=THEME_COLOR, fg='white')
        self.score_lavel.grid(column=1, row=0)

        self.canvas = Canvas(height=250, width=300, bg='white')
        self.question_text = self.canvas.create_text(
            150, 125, text="Question", fill=THEME_COLOR, font=('Arial', 20, 'italic'), width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        yes_button = PhotoImage(
            file='./100Days_Python_Projects/data/Day034_Quiz/images/true.png')
        self.correct_button = Button(
            image=yes_button, highlightthickness=0, command=self.true_pressed)
        self.correct_button.grid(column=0, row=2)

        false_button = PhotoImage(
            file='./100Days_Python_Projects/data/Day034_Quiz/images/false.png')
        self.wrong_button = Button(
            image=false_button, highlightthickness=0, command=self.false_pressed)
        self.wrong_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_lavel.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.question_text, text='You are done with the quiz!')
            self.yes_button.config(state='disable')
            self.wrong_button.config(state='disabled')

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer('True'))

    def false_pressed(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)
