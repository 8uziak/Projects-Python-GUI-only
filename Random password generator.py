import tkinter as tk
import random
import string 

# random password generator
def random_pass():

    new_password = ''
    
    rand_list = list(string.ascii_letters + string.digits)
    random.shuffle(rand_list)

    x = 0 
    for i in rand_list: 
        if x <= 10:
            new_password += i
            x += 1

    return new_password

# root window
root = tk.Tk()
root.geometry('300x200')
root.resizable(False, True)
root.title('Random password generator')


# button clicked
def btn_clicked():
    label = tk.Label(root,text=random_pass())
    label.pack()

button = tk.Button(root, text='Generate',command=btn_clicked)


button.pack()

root.mainloop()