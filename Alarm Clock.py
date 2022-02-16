from datetime import datetime
import tkinter as tk
from tkinter import ttk
import time



# loop
root = tk.Tk()
root.geometry('200x200')
root.resizable(False,False)
root.title('Alarm Clock')


# user input converter into date 
def func():
    user_inp_date = str(usr.get())
    date_time_obj = datetime.strptime(user_inp_date, '%d/%m/%y %H:%M')
    x = date_time_obj - datetime.now()
    t = int(x.total_seconds())
    while t:
        time.sleep(1)
        t-=1
    
    t1 = tk.Label(root,text='DING DONG!').grid(column=0,row=5)

# text
txt = tk.Label(root,text='Input should look like this\n> dd\mm\yy HH\MM <\nWake me up at: ')
txt.grid(column=0,row=0)

# user 
usr = tk.Entry(root, bg='yellow')
usr.grid(column=0,row=1)


# button 'submit'
button1 = tk.Button(root, text = 'Submit',command=func)
button1.grid(column=0,row=2)

# text
txt = tk.Label(root,text='(button goes blank\nafter clicking the button)')
txt.grid(column=0,row=6)

# End of loop
root.mainloop()
