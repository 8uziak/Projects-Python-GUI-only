import tkinter as tk
import random


root = tk.Tk()
root.geometry('230x150')
root.resizable(False,False)

# random number gen & label
i = random.randint(1,10)

i1 = 'For illustrative purposes,\nthe number that wins is:  ' + str(i)
tk.Label(root,text=i1).grid(column=0,row=6) 

# pop-up string "you lost"/"you won"
def gen(x): 
    
    if x == i:
        return 'You won'
    else: 
        return 'You lost'


# text
txt = tk.Label(root,text='    Guess a number (from 1 to 10): ')
txt.grid(column=0,row=0)

# user input (drop-down text)
variable = tk.IntVar(root)
variable.set(1) # default value

w = tk.OptionMenu(root, variable,
                1, 2, 3, 4, 5,
                6, 7, 8, 9, 10)

w.grid(column=0,row=1)



# button (when) clicked
def btn_clicked():
    num1 = variable.get()
    num2 = int(num1)
    label = tk.Label(root,text=gen(num2))
    label.grid(column=0,row=7)


# submit button
submit = tk.Button(root,text='Submit',command=btn_clicked)
submit.grid(column=0,row=4)

root.mainloop()