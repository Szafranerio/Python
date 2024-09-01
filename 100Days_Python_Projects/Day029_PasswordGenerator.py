from tkinter import *
from pathlib import Path
from tkinter import messagebox

FONT_NAME = "Courier"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = input_website.get()
    username = input_username.get()
    password = input_pass.get()


    if len(website) == 0 or len(password) == 0:
        warning = messagebox.showwarning(
            title="Warning", message='Check your data')
    else:
        is_ok = messagebox.askokcancel(
            title=website, message=f'Your details. \nEmail: {username} \nPassword: {password} \nIs it okey to save it?')
        if is_ok == True:
            with open('/Users/bartlomiejszafran/Desktop/data.txt', mode="a") as data_file:
                data_file.write(f"{website} | {username} | {password}\n")
                input_website.delete(0, END)
                input_pass.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=50, pady=50)
window.title("Password generator")

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_png = PhotoImage(
    file='/Users/bartlomiejszafran/Desktop/GitHub/Python/100Days_Python_Projects/data/Day029_Password/logo.png')
canvas.create_image(100, 100, image=lock_png)
canvas.grid(column=1, row=0)

website = Label(text='Website name', font=(FONT_NAME, 12))
website.grid(column=0, row=1)


username = Label(text='Email/Username', font=(FONT_NAME, 12))
username.grid(column=0, row=2)

password = Label(text='Password', font=(FONT_NAME, 12))
password.grid(column=0, row=3)

input_website = Entry(width=35)
input_website.grid(column=1, row=1, columnspan=2)
input_website.focus()

input_username = Entry(width=35)
input_username.grid(column=1, row=2, columnspan=2)
input_username.insert(0, 'bartekszafran@icloud.com')

input_pass = Entry(width=21)
input_pass.grid(column=1, row=3)

generate_button = Button(text='Generate Password')
generate_button.grid(column=2, row=3)

add_button = Button(text='Add', width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
