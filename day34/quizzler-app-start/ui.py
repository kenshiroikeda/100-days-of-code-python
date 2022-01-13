from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        canvas = Canvas(width=300, height=250, bg="WHITE", highlightthickness=0)
        canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=20)
        language_text = canvas.create_text(150, 125, text="Sample question text", font=("Arial", 18, "italic"))

        score_label = Label(text="Score: 0", bg=THEME_COLOR, highlightthickness=0, fg="WHITE", font=("Arial", 12))
        score_label.grid(column=1, row=0, padx=20, pady=20)

        true_image = PhotoImage(file="images/true.png")
        button_true = Button(image=true_image, highlightthickness=0)
        button_true.grid(row=2, column=0, padx=20, pady=20)

        false_image = PhotoImage(file="images/false.png")
        button_false = Button(image=false_image, highlightthickness=0)
        button_false.grid(row=2, column=1, padx=20, pady=20)


        self.window.mainloop()