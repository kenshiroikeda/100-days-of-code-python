from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_img)
language_text = canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="trouve", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

ng_image = PhotoImage(file="images/wrong.png")
button_ng = Button(image=ng_image, highlightthickness=0)
button_ng.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
button_right = Button(image=right_image, highlightthickness=0)
button_right.grid(row=1, column=1)

window.mainloop()