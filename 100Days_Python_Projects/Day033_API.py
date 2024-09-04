import random
from tkinter import *
import requests

#response_ISS = requests.get(url='http://api.open-notify.org/iss-now.json')
#print(response_ISS)
#
#response_ISS.raise_for_status()
#data = response_ISS.json()
#print(data)
#
#position_iss = data['iss_position']
#print(position_iss)
#
#lat_position_iss = data['iss_position']['latitude']  # Specific data
#print(lat_position_iss)
#
## Kanye Rest
#def get_quote():
#    global flip_timer
#    window.after_cancel(flip_timer)
#    texts = requests.get(url='https://api.kanye.rest')
#    texts.raise_for_status()
#    data = texts.json()
#    canvas.itemconfig(quote_text, text=data['quote'])
#    flip_timer = window.after(3000, func=get_quote)
#
#
#window = Tk()
#window.title("Kanye Says...")
#window.config(padx=50, pady=50)
#
#flip_timer = window.after(3000, func=get_quote)
#
#canvas = Canvas(width=300, height=414)
#background_img = PhotoImage(
#    file='/Users/bartlomiejszafran/Desktop/GitHub/Python/100Days_Python_Projects/data/Day033_API/background.png')
#canvas.create_image(150, 207, image=background_img)
#quote_text = canvas.create_text(
#    150, 207, text='Word', width=250, font=("Arial", 30, "bold"), fill="white")
#canvas.grid(row=0, column=0)
#
#kanye_img = PhotoImage(
#    file="/Users/bartlomiejszafran/Desktop/GitHub/Python/100Days_Python_Projects/