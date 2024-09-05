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
#    file="/Users/bartlomiejszafran/Desktop/GitHub/Python/100Days_Python_Projects/data/Day033_API/kanye.png")
#kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
#kanye_button.grid(row=1, column=0)
#
#get_quote()
#window.mainloop()
#
#ISS Check
from datetime import datetime
#MY_LAT = 57.046707
#MY_LNG = 9.935932
#
#parameters = {
#    'lat': MY_LAT,
#    'lng': MY_LNG,
#    'formatted': 0,
#}
#response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
#response.raise_for_status()
#data = response.json()
#sunrise = data['results']['sunrise']
#sunset = data['results']['sunset']
#
#
#time_now = datetime.now()
#
#print(sunrise.split("T")[1].split(":")[0])
#print(sunset.split("T")[1].split(":")[0])
#print(time_now.hour)
#

#ISS location

MY_LAT = 57.046707
MY_LNG = 9.935932

parameters = {
    'lat': MY_LAT,
    'lng': MY_LNG,
    'formatted': 0,
}
def iss_overhead():
    response_ISS = requests.get(url='http://api.open-notify.org/iss-now.json')

    response_ISS.raise_for_status()
    data = response_ISS.json()

    iss_latitiude = float(data['iss_position']['latitude'])
    iss_longitude = float(data['iss_position']['longitude'])

    if MY_LAT - 5 <= iss_latitiude  <= MY_LAT + 5 and MY_LNG - 5 <= iss_longitude <= MY_LNG + 5:
        return True

def is_night():
    parameters = {
        'lat': MY_LAT,
        'lng': MY_LNG,
        'formatted': 0
    }
    response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data['results']['sunrise'].split("T")[1].split(":")[0])
    sunset = int(data['results']['sunset'].split("T")[1].split(":")[0])
    time_now = datetime.now().hour
    
    if time_now >= sunset or time_now <= sunrise:
        return 
    
