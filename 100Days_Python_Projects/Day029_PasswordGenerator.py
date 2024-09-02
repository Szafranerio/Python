from tkinter import *
from pathlib import Path
from tkinter import messagebox
import json
from random import choice, randint, shuffle


FONT_NAME = "Courier"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

import pyperclip
def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    pass_letters = [choice(letters) for _ in range(randint(8, 10))]
    pass_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    pass_num = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = pass_letters + pass_symbols + pass_num
    shuffle(password_list)
    password = "".join(password_list)

    input_pass.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = input_website.get()
    username = input_username.get()
    password = input_pass.get()
    new_data = {
        website: {
            "email": username,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Warning", message="Check your data")
        return

    try:
        
        try:
            with open('/Users/bartlomiejszafran/Desktop/data.json', mode="r") as data_file:
                data = json.load(data_file)
        except json.JSONDecodeError:
            data = {}
        except FileNotFoundError:
            data = {}
        
        data.update(new_data)

        with open('/Users/bartlomiejszafran/Desktop/data.json', mode="w") as data_file:
            json.dump(data, data_file, indent=4)
            
    except Exception as e:
        messagebox.showerror(title="Error", message=f"An error occurred: {e}")
    finally:
        input_website.delete(0, END)
        input_pass.delete(0, END)
            
def check_password():
    website = input_website.get()
    try:
        with open('/Users/bartlomiejszafran/Desktop/data.json') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title='Error', message='No Data')
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=website, message=f'Email: {email}\n Password: {password}')
        else:
            messagebox.showinfo(title='Error', message=f'No details for {website}')
            
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.config(padx=50, pady=50)
window.title("Password generator")

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_png = PhotoImage(
    file='/Users/bartlomiejszafran/Desktop/Git