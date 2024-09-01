import tkinter

window = tkinter.Tk()
window.title('GUI Program')
window.minsize(width=500, height=300)

#Label
my_label = tkinter.Label(text='Label', font=('Arial', 24, 'bold'))
my_label.pack()

#Entry
input = tkinter.Entry(width=10)
input.pack()

#Buttons
def button_clicked():
    print('I got clicked')
    new_text = input.get()
    my_label.config(text=new_text)
    
button = tkinter.Button(text='Click here', command=button_clicked)
button.pack()















#At the end always
window.mainloop()
    