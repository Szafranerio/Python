from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try :
    danish_data = pandas.read_csv('./data/Day031_FlashCards/data/words_to_learn.csv')
except FileNotFoundError:
    orignal_data = pandas.read_csv('./data/Day031_FlashCards/data/danish_words.csv')
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = danish_data.to_dict(orient='records')



def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text='Danish', fill='black')
    canvas.itemconfig(card_word, text=current_card['Danish'], fill='black')
    canvas.itemconfig(card_background, image=front_card)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=current_card['English'], fill='white')
    canvas.itemconfig(card_background, image=back_card)
    
def is_known():
    to