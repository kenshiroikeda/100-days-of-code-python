from tkinter import *
import pandas
import random
import os

from pandas.errors import EmptyDataError

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

CARD_IMG = PhotoImage(file="images/card_front.png")
AWS_IMG = PhotoImage(file="images/card_back.png")
card_img = None
word_text = None
language_text = None
timer = None
dict_word = None
ORG_FILE_PATH = "data/french_words.csv"
UPD_FILE_PATH = "data/words_to_learn.csv"

try:
    df = pandas.read_csv(UPD_FILE_PATH)
except FileNotFoundError:
    df = pandas.read_csv(ORG_FILE_PATH)
except EmptyDataError:
    df = pandas.read_csv(ORG_FILE_PATH)
finally:
    french_dict = df.to_dict('records')


def show_answer(word):
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=word["English"], fill="white")
    canvas.itemconfig(card_img, image=AWS_IMG)


def set_new_word():
    global timer, dict_word
    if timer is not None:
        window.after_cancel(timer)
    dict_word = random.choice(french_dict)
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=dict_word["French"], fill="black")
    canvas.itemconfig(card_img, image=CARD_IMG)
    timer = window.after(3000, show_answer, dict_word)


def correct():
    french_dict.remove(dict_word)
    removed_df = pandas.DataFrame.from_dict(french_dict)
    removed_df.to_csv(UPD_FILE_PATH, index=False)
    set_new_word()


def ng():
    non_removed_df = pandas.DataFrame.from_dict(french_dict)
    non_removed_df.to_csv(UPD_FILE_PATH, index=False)
    set_new_word()


canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_img = canvas.create_image(400, 263, image=card_img)
language_text = canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="trouve", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

ng_image = PhotoImage(file="images/wrong.png")
button_ng = Button(image=ng_image, highlightthickness=0, command=ng)
button_ng.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
button_right = Button(image=right_image, highlightthickness=0, command=correct)
button_right.grid(row=1, column=1)

set_new_word()

window.mainloop()