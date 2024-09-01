import tkinter

window = tkinter.Tk()
window.title('GUI Program')
window.minsize(width=500, height=300)

#Label
my_label = tkinter.Label(text='Label', font=('Arial', 24, 'bold'))
my_label.grid(column=0,row=0)

#Entry
input = tkinter.Entry(width=10)
input.grid(column=2, row=2)

#Buttons
def button_clicked():
    print('I got clicked')
    new_text = input.get()
    my_label.config(text=new_text)
    
button = tkinter.Button(text='Click here', command=button_clicked)
button.grid(column=1, row=1)

button_1 = tkinter.Button(text='New Button')
button_1.grid(column=2, row=0)















#At the end always
window.mainloop()
    