import tkinter as tk
import random

# global word to guess and list out of it
word_to_guess= ''
wg_list = []

# taking 1 random word out of 267751 words (from words.txt file)
def ran_word():
    
    global word_to_guess
    global wg_list

    with open('words.txt', 'r') as f:
        
        f_random = random.randint(1,267751)
        
        for i in range(1,f_random): 
            
            f.readline()
            
        word_to_guess = f.readline()
        wg_list = list((('_') * (len(word_to_guess) - 1)))    


# hangman drawings
hangman_1 = "---"
hangman_2 = '\n | ' + '\n | ' + '\n | ' + '\n | ' + '\n | ' + '\n | ' + "\n---" 
hangman_3 = '\n  ________''\n |' + '\n | ' + '\n | ' + '\n | ' + '\n | ' + '\n | ' + "\n---" 
hangman_4 = '\n  ________''\n |       |' + '\n |       O' + '\n | ' + '\n | ' + '\n | ' + '\n | ' + "\n---"
hangman_5 = '\n  ________''\n |       |' + '\n |       O' + '\n |       |' + '\n | ' + '\n | ' + '\n | ' + "\n---"
hangman_6 = '\n  ________''\n |       |' + '\n |       O' + '\n |      /|\ ' + '\n |      / \ ' + '\n | ' + '\n | ' + "\n---"
    
hangman_lst = ['', hangman_1, hangman_2,hangman_3, hangman_4,hangman_5,hangman_6]

###        
display_text = ''
wg_global = ''
wrong = 0

# checking if user's input is correct or not
def check():

    # globals
    global word_to_guess
    global wrong 
    global hangman_lst
    global wg_list

    if usr.get().upper() in word_to_guess:
        print('nice')
        n = 0 

        for i in range(1,len(word_to_guess)):
                if usr.get().upper() == word_to_guess[n]:
                    wg_list[n] = usr.get().upper()
                    n += 1
                else:    
                    n += 1
        
        if wg_list == (list(word_to_guess))[:-1]:

            words_guessed.config(text='YOU WON!!!!')
            display_hang.config(text=f'You missed {wrong} time(s)')

        else:
            words_guessed.config(text=wg_list)

    else:

        wrong += 1
        dis = hangman_lst[wrong]
        display_hang.config(text = dis)

        if wrong == 6: 
            words_guessed.config(text='You lost')

# reset the game / new game
def newGame():
    
    global wrong 

    ran_word()
    wrong = 0
    display_hang.config(text=dis)
    words_guessed.config(text=wg_list)
    admin.config(text=f"***\nadmins functionality,\ncorrect answer is: {word_to_guess} \n***")

# driver code
if __name__ == "__main__":
    
    
    ran_word()
    # start LOOP
    root = tk.Tk()
    root.geometry("600x300")
    root.resizable(False,False)
    root.title('Hangman')

    # row to draw a hangman

    dis = ''
    display_hang = tk.Label(root,text=dis)
    display_hang.grid(column=0,row=4)

    # row with guessed words
    words_guessed = tk.Label(root,text=wg_list)
    words_guessed.grid(column=0,row=3)

    # text 
    txt = tk.Label(root, text= 'Welcome to Hangman Game!\nPut a letter or a word in a box bellow\n(lowercase and capital letters are accepted)')
    txt.grid(column=0,row=0)

    # user's input
    usr = tk.Entry(root)
    usr.grid(column=0,row=1)

    # submit button
    btn_submit = tk.Button(root, text='Submit', command=check)
    btn_submit.grid(column=0,row=2)

    # admin functionality
    admin = tk.Label(root,text=f"***\nadmins functionality,\ncorrect answer is: {word_to_guess} \n***")
    admin.grid(column=2, row=0)
    
    # new game button
    btn_again = tk.Button(root,text='new game',command=newGame)
    btn_again.grid(column=1,row=2)

    root.mainloop()