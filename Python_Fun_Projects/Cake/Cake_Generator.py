from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo
import json
import os
import pandas


def show_help():
    msg = messagebox.showinfo('Help', 'Chose the type of weight and input the original recipe ingredtiens. Sum up with the amount of pieces and see how much do you need!')


def add():
    original_portion = input_original.get()
    weight = input_weight.get()
    name = input_product_name.get()
    aimed_amount = input_aimed.get()

    # Check and convert input fields
    try:
        original_portion = float(original_portion)
    except ValueError:
        messagebox.showwarning(title="Warning", message="It must be a number!")
        return

    try:
        weight = float(weight)
    except ValueError:
        messagebox.showwarning(title="Warning", message="It must be a number!")
        return

    try:
        name = str(name)
    except ValueError:
        messagebox.showwarning(title="Warning", message="It must be a name!")
        return

    # Data to be added
    new_data = {
        "selection": {
            "Num_of_portions": original_portion,
            "aimed_portion": aimed_amount,
            "name": name,
            "weight": weight
        
        }
    }

    # Get absolute path to the data.json file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_file_path = os.path.join(script_dir, 'data', 'data.json')

    try:
        data_file_path = './data/data.json'
        try:
            with open(data_file_path, mode="r") as data_file:
                data = json.load(data_file)
        except json.JSONDecodeError:
            data = {}

        data.append(new_data)

        # Write updated data back to the file
        with open(data_file_path, mode="w") as data_file:
            json.dump(data, data_file, indent=4)

    except Exception as e:
        messagebox.showerror(title="Error", message=f"An error occurred: {e}")
    finally:
        # Clear the input fields
        input_weight.delete(0, END)
        input_product_name.delete(0, END)
     
        

def ready():
    pass


def save_products():
    pass

data = pandas.read_json('./data/data.json')
print(data)

# UI
window = Tk()
window.config(padx=25, pady=25)
window.geometry('600x600')
window.title('Cake Converter')

# Info table
original_portions = Label(window, text='For how many portions this recipe is?')
original_portions.grid(column=0, row=1, columnspan=1, padx=10, pady=5)
input_original = Entry()
input_original.grid(column=1, row=1, columnspan=1, padx=10, pady=5)

weight = Label(window, text="Pick amount and weight: ")
weight.grid(column=0, row=2)
input_weight = Entry()
input_weight.grid(column=1, row=2, columnspan=1, padx=10, pady=5)

type = StringVar()
type.set('Grams')
dropdown = OptionMenu(window, type, "Grams", "Ml")
dropdown.grid(column=2, row=2, columnspan=1, padx=10, pady=5)

product = Label(window, text='What kind of product: ')
product.grid(column=0, row=3)
input_product_name = Entry()
input_product_name.grid(column=1, row=3)

aimed_amount = Label(window, text='For how many portions this recipe is?')
aimed_amount.grid(column=0, row=5, columnspan=1, padx=10, pady=5)
input_aimed = Entry()
input_aimed.grid(column=1, row=5, columnspan=1, padx=10, pady=5)


# Buttons
help_button = Button(window, text='Help?', font=(
    'arial, 12'), command=show_help)
help_button.grid(column=0, row=6, padx=10, pady=5)

add_button = Button(window, text='Add', font=('arial, 12'), command=add)
add_button.grid(column=1, row=6, padx=10, pady=5)

ready_button = Button(window, text='Ready', font=('arial, 12'))
ready_button.grid(column=2, row=6, padx=10, pady=5)


window.mainloop()
