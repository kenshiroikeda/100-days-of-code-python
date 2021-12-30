from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    label_title.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    label_checkmark.config(text="✓")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    if (reps % 8 == 0) & (reps != 0):
        label_title.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN)
    elif reps % 2 == 0:
        count_down(WORK_MIN)
        label_title.config(text="Work", fg=GREEN)
    else:
        count_down(SHORT_BREAK_MIN)
        label_title.config(text="Break", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps
    global timer
    count_min = str(math.floor(count / 60)).zfill(2)
    count_sec = str(count % 60).zfill(2)
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        if reps % 2 == 0:
            text_checkmark = "✓"
            for i in range(math.floor(reps / 2)):
                text_checkmark = text_checkmark + "✓"
            label_checkmark.config(text=text_checkmark)
        reps += 1
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=30, bg=YELLOW)

label_title = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
label_title.grid(row=0, column=1)

canvas = Canvas(width=250, height=270, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(125, 150, image=tomato_img)
timer_text = canvas.create_text(125, 170, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

button_start = Button(text="Start", command=start_timer)
button_start.grid(row=2, column=0)

button_end = Button(text="Reset", command=reset_timer)
button_end.grid(row=2, column=2)

label_checkmark = Label(text="✓", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 12, "bold"))
label_checkmark.grid(row=3, column=1)

window.mainloop()
