from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

danish_data = pandas.read_csv('./data/Day031_FlashCards/data/danish_words.csv')
to_learn = danish_data.to_dict(orient='records')
current_card = {}


def next_card():
    global current_card
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text='Danish')
    canvas.itemconfig(card_word, text=current_card['Danish'])


def flip_card():
    canvas.itemconfig(card_title, text='English')
    canvas.itemconfig(card_word, text=current_card['English'])
    canvas.itemconfig(card_background, image=back_card)

# User Interface


window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title('Flash Cards')

window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0)
front_card = PhotoImage(file='./data/Day031_FlashCards/images/card_front.png')
back_card = PhotoImage(file='./data/Day031_FlashCards/images/card_back.png')
card_background = canvas.create_image(400, 263, image=front_card)
card_title = canvas.create_text(
    400, 150, text='Title', font=('Ariel', 40, 'italic'))
card_word = canvas.create_text(
    400, 263, text='WORD', font=('Ariel', 60, 'bold'))
canvas.config(bg=BACKGROUND_COLOR)
canvas.grid(column=0, row=0, columnspan=2)

# Button images
ok_button = PhotoImage(file='./data/Day031_FlashCards/images/right.png')
false_button = PhotoImage(file='./data/Day031_FlashCards/images/wrong.png')
correct_button = Button(
    image=ok_button, highlightthickness=0, command=next_card)
correct_button.grid(column=1, row=2)
wrong_button = Button(image=false_button, highlightthickness=0)
wrong_button.grid(column=0, row=2)

next_card()

window.mainloop()
