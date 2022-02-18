import tkinter as tk
import time

# start LOOP
root = tk.Tk()
root.geometry("300x100")
root.resizable(False,False)

# CLOCK function
def clockRoot():
    t = time.strftime('%H:%M:%S')
    y.config(text = t)
    y.after(1000, clockRoot)

# customezing CLOCK function
y = tk.Label(
            root,
            anchor='center', 
            bg='white',
            font= ('DejaVuSans-Bold',44),
            height="100",
            width="100",
            )

# displaying func
y.pack()
clockRoot()

# end LOOP
root.mainloop()