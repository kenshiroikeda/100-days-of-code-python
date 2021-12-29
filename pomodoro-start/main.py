import tkinter
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100 ,pady=30, bg=YELLOW)

label_title = Label(text="Timer",fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
label_title.grid(row=0, column=1)

canvas = Canvas(width=250, height=270, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(125, 150, image=tomato_img)
canvas.create_text(125, 170, text="00:00",fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

button_start = Button(text="Start")
button_start.grid(row=2, column=0)

button_end = Button(text="Reset")
button_end.grid(row=2, column=2)

label_checkmark = Label(text="✓",fg=GREEN, bg=YELLOW, font=(FONT_NAME, 12, "bold"))
label_checkmark.grid(row=3, column=1)

window.mainloop()
