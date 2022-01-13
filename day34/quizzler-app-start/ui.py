from functools import partial
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="WHITE", highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.language_text = self.canvas.create_text(150, 125, text="Sample question text", font=("Arial", 18, "italic"),width=280)

        self.get_next()

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, highlightthickness=0, fg="WHITE", font=("Arial", 12))
        self.score_label.grid(column=1, row=0, padx=20, pady=20)

        true_image = PhotoImage(file="images/true.png")
        self.button_true = Button(image=true_image, highlightthickness=0, command=partial(self.check_answer, "true"))
        self.button_true.grid(row=2, column=0, padx=20, pady=20)

        false_image = PhotoImage(file="images/false.png")
        self.button_false = Button(image=false_image, highlightthickness=0, command=partial(self.check_answer, "false"))
        self.button_false.grid(row=2, column=1, padx=20, pady=20)

        self.window.mainloop()

    def get_next(self):
        self.canvas.config(bg="white")
        if self.quiz_brain.still_has_questions():
            question = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.language_text, text=question)
        else:
            self.canvas.itemconfig(self.language_text, text="You've reached end of quiz")
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")

    def check_answer(self, answer):
        self.give_feedback(self.quiz_brain.check_answer(answer))

    def give_feedback(self, is_correct: bool):
        if is_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.score_label.config(text=f"Score: {self.quiz_brain.score}")
        self.window.after(1000, self.get_next)







