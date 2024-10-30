from tkinter import *
import html
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
LABEL_FONT = ("Comic Sans", 12, "bold")
QUESTION_FONT = ("Arial", 20, "italic")

class QuizInterface:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.is_correct = False
        self.text = ""

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Score label
        self.score_l = Label(master=self.window, text="Score: 0")
        self.score_l.config(bg=THEME_COLOR, fg="white", font=LABEL_FONT)
        self.score_l.grid(column=1, row=0)

        # Question label
        self.question_l = Label(master=self.window, text="")
        self.question_l.config(bg=THEME_COLOR, fg="white", font=LABEL_FONT)
        self.question_l.grid(column=0, row=0)

        # Canvas
        self.canvas = Canvas(master=self.window, width=300, height=250)
        self.canvas.config(bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280, text="", font=QUESTION_FONT, fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)

        # True button
        true_img = PhotoImage(file="images/true.png")

        self.true_b = Button(master=self.window, image=true_img, command=self.true_button_action)
        self.true_b.config(highlightthickness=0, bd=0)
        self.true_b.grid(column=0, row=2)

        # False button
        false_img = PhotoImage(file="images/false.png")

        self.false_b = Button(master=self.window, image=false_img, command=self.false_button_action)
        self.false_b.config(highlightthickness=0, bd=0)
        self.false_b.grid(column=1, row=2)

        self.show_question()

        self.window.mainloop()  # Any loop from the main file must be removed or there will be conflict

    def true_button_action(self):
        self.is_correct = self.quiz.check_answer("true")
        self.give_feedback()

    def false_button_action(self):
        self.is_correct = self.quiz.check_answer("false")
        self.give_feedback()

    def show_question(self):
        self.canvas.config(bg="white")
        if self.is_correct:
            self.update_score()
        if self.quiz.still_has_questions():
            self.text = self.quiz.next_question()
            self.update_question()
            self.canvas.itemconfig(self.question_text, text=f"{html.unescape(self.text)}")
        else:
            self.true_b.config(state="disabled")
            self.false_b.config(state="disabled")
            self.canvas.itemconfig(self.question_text, text=f"Your have answered all questions!")

    def update_question(self):
        self.question_l.config(text=f"Question: {self.quiz.question_number}")

    def update_score(self):
        self.score_l.config(text=f"Score: {self.quiz.score}")

    def give_feedback(self):
        if self.is_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, func=self.show_question)
