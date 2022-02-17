import tkinter as tk
import webbrowser


# start LOOP
root = tk.Tk()
root.title('Pig Latin (language generator)')
root.geometry('200x200')

# beginning text
txt = tk.Label(root,text='Welcome to Pig Latin game!\nEnter your word')
txt.grid(column=0,row=0)

# user input
usr = tk.Entry(root,cursor='dot')
usr.grid(column=0,row=1)

def pig_Latin(xd):

    usr_list = list(xd.get())

    final_word = ''

    vowel = ["a", "e", "y", "i", "o", "u"]
    consonant = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "r", "s", "t", "w", "y"]

    ay = ["a","y"]
    yay =  ["y","a","y"]

    # putting word apart and making it 'Pig Latin'
    if usr_list[0] in consonant and usr_list[1] in vowel:
        x = usr_list[1:] 
        x.extend(usr_list[0])
        x.extend(ay)

    elif usr_list[0] in vowel and usr_list[1] in vowel:
        x = usr_list
        x.extend(yay)

    else:
        x = usr_list[2:]
        x.extend(usr_list[0:1])
        x.extend(ay)
    
    # creating final result
    for j in x:
        final_word += j 
    
    tk.Label(root,text=final_word).grid(column=0,row=4) # putting result on the screen 

# action SUBMIT button
def btn_submit_action():
    usr_wrote = tk.Label(root,comand=pig_Latin(usr))

# SUBMIT button 
btn_submit =  tk.Button(root,text='Submit',command=btn_submit_action)
btn_submit.grid(column=0,row=3)

# action rules
def btn_rules_action():
    web = webbrowser.open('https://en.wikipedia.org/wiki/Pig_Latin')  # redirectin to webside with rules 
    func_button = tk.Label(root,command=web)

# rules button
btn_rules =  tk.Button(root,text='rules for Pig Latin',command=btn_rules_action)
btn_rules.grid(column=0,row=7)

# end LOOP
root.mainloop()