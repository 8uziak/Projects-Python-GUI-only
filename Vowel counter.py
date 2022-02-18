import tkinter as tk

# start LOOP
root = tk.Tk()
root.title('Vowel counter')
root.geometry("215x300")

# text
txt = tk.Label(root,text='Welcome to VOWEL COUNTER \nput your word or sentance below')
txt.grid(column=0,row=0)

# usr input
usr_inp =  tk.Entry(root,cursor='circle')
usr_inp.grid(column=0,row=1)

# action for SUBMIT button
def btn_sbmt_action():
    lett_counter = 0
    vowel = ("a", "e", "i", "o", "u")
    b = list(usr_inp.get().replace(" ",""))
    for i in b:
        if i.lower() in vowel:
            lett_counter += 1
        
    tk.Label(root,text = lett_counter).grid(column=0,row=4)


# SUBMIT button
btn_sbmt = tk.Button(root,text='Submit',command=btn_sbmt_action)
btn_sbmt.grid(column=0,row=2)

# end LOOP
root.mainloop()

