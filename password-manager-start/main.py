from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

FONT_NAME = "Courier"
PATH_TXT = "data.json"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)

    print(f"Your password is: {password}")
    txt_password.delete(0, END)
    txt_password.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def clear():
    txt_website.delete(0, END)
    txt_password.delete(0, END)
    txt_website.focus()


def show_no_detail_message():
    messagebox.showwarning(title="warning", message="No details for the website exists.")


def find_password():
    str_website = txt_website.get()
    try:
        with open(PATH_TXT, 'r') as datafile:
            data = json.load(datafile)
    except FileNotFoundError:
        print('file does not exist')
        show_no_detail_message()
    else:
        if str_website in data :
            saved_email = data[str_website]["email"]
            saved_password = data[str_website]["password"]
            messagebox.showinfo(title=str_website, message=f"Email: {saved_email} \n Password: {saved_password}")
        else:
            show_no_detail_message()


def save():
    str_website = txt_website.get()
    str_email = txt_email.get()
    str_password = txt_password.get()
    new_data = {
        str_website: {
            "email": str_email,
            "password": str_password
        }
    }
    if validate(str_website, str_email, str_password):
        is_ok = messagebox.askokcancel(title=str_website, message=f"These are the details entered: \n Email:{str_email}"
                                                                  f" \nPassword: {str_password}\n Is it OK to save?")
        if is_ok:
            try:
                with open(PATH_TXT, 'r') as datafile:
                    data = json.load(datafile)
            except FileNotFoundError:
                with open(PATH_TXT, 'w') as datafile:
                    print('create file')
                    json.dump(new_data, datafile, indent=4)
            else:
                data.update(new_data)
                with open(PATH_TXT, 'w') as datafile:
                    json.dump(data, datafile, indent=4)
            finally:
                clear()

def validate(str_website, str_email, str_password):
    if str_website == "" or str_email == "" or str_password == "":
        messagebox.showwarning(title="Warning", message=f"Please do not leave any fields empty!!")
        return False
    else:
        return True


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

label_website = Label(text="Website:", justify=RIGHT)
label_website.grid(row=1, column=0)

txt_website = Entry(width=32, justify=LEFT)
txt_website.grid(sticky=W, row=1, column=1, columnspan=2)

button_search = Button(text="Search",width=14,command=find_password)
button_search.grid(sticky=W, row=1, column=2)

label_email = Label(text="Email/Username:", justify=RIGHT)
label_email.grid(row=2, column=0)

txt_email = Entry(width=52, justify=LEFT)
txt_email.grid(sticky=W, row=2, column=1, columnspan=2)

label_password = Label(text="PassWord:", justify=RIGHT)
label_password.grid(row=3, column=0)

txt_password = Entry(width=32, justify=LEFT)
txt_password.grid(sticky=W, row=3, column=1)

button_generate = Button(text="Generate Password", anchor="w", command=generate_password)
button_generate.grid(sticky=W, row=3, column=2)

button_add = Button(text="Add", width=44, command=save)
button_add.grid(sticky=W, row=4, column=1, columnspan=2)

window.mainloop()
