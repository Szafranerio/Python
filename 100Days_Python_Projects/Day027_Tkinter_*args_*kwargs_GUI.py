import tkinter

#window = tkinter.Tk()
#window.title('GUI Program')
#window.minsize(width=500, height=300)
#
##Label
#my_label = tkinter.Label(text='Label', font=('Arial', 24, 'bold'))
#my_label.grid(column=0,row=0)
#
##Entry
#input = tkinter.Entry(width=10)
#input.grid(column=2, row=2)
#
##Buttons
#def button_clicked():
#    print('I got clicked')
#    new_text = input.get()
#    my_label.config(text=new_text)
#    
#button = tkinter.Button(text='Click here', command=button_clicked)
#button.grid(column=1, row=1)
#
#button_1 = tkinter.Button(text='New Button')
#button_1.grid(column=2, row=0)

#Converter project

window = tkinter.Tk()
window.title('GUI Program')
window.minsize(width=500, height=300)

input = tkinter.Entry(width=10)
input.grid(column=1,row=0)

miles = tkinter.Label(text='miles')
miles.grid(column=2,row=0)

is_equal = tkinter.Label(text='is equal to: ')
is_equal.grid(column=0, row=2)

value = tkinter.Label(text = 0)
value.grid(column=1, row=2)

km = tkinter.Label(text='km')
km.grid(column=2, row=2)

def convertor():
    new_value = float(input.get()) * 1.609
    value.config(text=new_value)

button = tkinter.Button(text='Calculate', command=convertor)
button.grid(column=1, row=3)









#At the end always
window.mainloop()
    