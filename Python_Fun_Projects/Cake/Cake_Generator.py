from tkinter import *
from tkinter import messagebox
import json
import os
import pandas

data = []

def show_help():
    messagebox.showinfo('Help', 'Choose the type of weight and input the original recipe ingredients. Sum up with the amount of pieces and see how much you need!')

def add():
    original_portion = input_original.get()
    weight = input_weight.get()
    name = input_product_name.get()
    aimed_amount = input_aimed.get()

    # Validate the weight input as a number
    try:
        weight = float(weight)
    except ValueError:
        messagebox.showwarning(title="Warning", message="Weight must be a number!")
        return

    if not name:
        messagebox.showwarning(title="Warning", message="Product name cannot be empty!")
        return

    new_data = {
        "name": name,
        "weight": weight
    }

    try:
        data_file_path = './data/data.json'

        # Ensure the directory exists
        if not os.path.exists('./data'):
            print("Creating data directory...")
            os.makedirs('./data')

        # Check if the file exists
        if os.path.exists(data_file_path):
            print("Loading existing data...")
            try:
                with open(data_file_path, mode="r") as data_file:
                    data = json.load(data_file)
                    print(f"Existing data: {data}")
            except json.JSONDecodeError:
                print("Failed to decode JSON, initializing empty list...")
                data = []
        else:
            print("Data file does not exist, initializing empty list...")
            data = []

        # Append the new data to the list
        data.append(new_data)
        print(f"Appending new data: {new_data}")

        # Write the updated data back to the file
        with open(data_file_path, mode="w") as data_file:
            json.dump(data, data_file, indent=4)
            print("Data saved successfully!")

        messagebox.showinfo(title="Success", message="Data saved successfully!")

    except Exception as e:
        messagebox.showerror(title="Error", message=f"An error occurred: {e}")
    finally:
        input_weight.delete(0, END)
        input_product_name.delete(0, END)
        
data = pandas.read_json('./data/data,json')
print(data)

# UI setup
window = Tk()
window.config(padx=25, pady=25)
window.geometry('600x600')
window.title('Cake Converter')

# Info table
Label(window, text='For how many portions this recipe is?').grid(column=0, row=1, padx=10, pady=5)
input_original = Entry(window)
input_original.grid(column=1, row=1)

Label(window, text="Pick amount and weight: ").grid(column=0, row=2)
input_weight = Entry(window)
input_weight.grid(column=1, row=2)

Label(window, text='What kind of product: ').grid(column=0, row=3)
input_product_name = Entry(window)
input_product_name.grid(column=1, row=3)

Label(window, text='For how many portions do you need?').grid(column=0, row=5)
input_aimed = Entry(window)
input_aimed.grid(column=1, row=5)

Button(window, text='Help?', command=show_help).grid(column=0, row=6)
Button(window, text='Add', command=add).grid(column=1, row=6)

window.mainloop()
