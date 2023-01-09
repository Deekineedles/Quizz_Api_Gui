from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)
        self.canvas = Canvas()
        self.canvas.config(width=300, height=250)
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="Text goes here",
            font=FONT,
            fill=THEME_COLOR,
            width=280,
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20, padx=20)
        self.score = Label(text="Score: ", fg="white", bg=THEME_COLOR)
        self.score.grid(row=0, column=1)
        self.check_mark_button = PhotoImage(file="images/true.png")
        self.check_button = Button(image=self.check_mark_button, command=self.right)
        self.check_button.grid(column=0, row=2)
        self.false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_image, command=self.wrong)
        self.false_button.grid(column=1, row=2)
        self.get_next_question()

    def right(self):
        self.give_feedback(self.quiz.check_answer("True"))
    def wrong(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)



    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.check_button.config(state="disabled")
            self.false_button.config(state="disabled")


        self.window.mainloop()