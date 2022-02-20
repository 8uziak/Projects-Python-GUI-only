import tkinter as tk
import math
import random

# default display value
display_num = ""


# press functionality for buttons 
def press(num):
	
	global display_num

	display_num = display_num + str(num)

	equation.set(display_num)

# action = button
def equalpress():

	try:

		global display_num

		total = str(eval(display_num))

		equation.set(total)

		display_num = ""

	except:

		equation.set(" error ")
		display_num = ""

# action 1/x button
def oneDivX():

	global display_num

	total = str(eval("1/" + display_num))

	equation.set(total)

	display_num = ""

# action x^2 button
def powNum():

	global display_num

	total = str(math.pow(eval(display_num),2))

	equation.set(total)

	display_num = ""

# action x^3 button
def powThreeNum():

	global display_num

	total = str(math.pow(eval(display_num),3))

	equation.set(total)

	display_num = ""

# action +/- button
def posNegNum():
    
    global display_num
        
    display_num = str(-(eval(display_num)))

    equation.set(display_num)
    
# action ! button
def factorialNum():

    global display_num
    
    total = str(math.factorial(eval(display_num)))
    equation.set(total)
    display_num = ""

# action square root button
def squareNum():

    global display_num
    
    total = str(math.sqrt(eval(display_num)))
    equation.set(total)
    display_num = ""

# action % button
def percentageNum():

    global display_num
    
    total = str((eval(display_num)/100))
    equation.set(total)
    display_num = ""

# action log(2) button
def logNum():

    global display_num
    
    total = str(math.log(eval(display_num),2))
    equation.set(total)
    display_num = ""

# action ln button
def lnNum():

    global display_num
    
    total = str(math.log(eval(display_num)))
    equation.set(total)
    display_num = ""

# action sin button
def sinNum():

    global display_num
    
    total = str(math.sin(eval(display_num)))
    equation.set(total)
    display_num = ""

# action cos button
def cosNum():

    global display_num
    
    total = str(math.cos(eval(display_num)))
    equation.set(total)
    display_num = ""

# action tan button
def tanNum():

    global display_num
    
    total = str(math.tan(eval(display_num)))
    equation.set(total)
    display_num = ""

# action sinH button
def sinhNum():

    global display_num
    
    total = str(math.sinh(eval(display_num)))
    equation.set(total)
    display_num = ""

# action cosH button
def coshNum():

    global display_num
    
    total = str(math.cosh(eval(display_num)))
    equation.set(total)
    display_num = ""

# action tanH button
def tanhNum():

    global display_num
    
    total = str(math.tanh(eval(display_num)))
    equation.set(total)
    display_num = ""

# action eX button
def exNum():

    global display_num
    
    total = str(math.exp(eval(display_num)))
    equation.set(total)
    display_num = ""

# active C button to clear output
def clear():
	global display_num
	display_num = ""
	equation.set("")


# driver code
if __name__ == "__main__":

    #start of Loop
    root = tk.Tk()
    root.title('Calculator')

    equation = tk.StringVar() # holds a string


    display_num_update = tk.Entry(root, text=equation) # well... it's display
    display_num_update.grid(column=8, row=1)
    
    # 1/x button
    btn_1x = tk.Button(root,text='1/x',command=oneDivX)
    btn_1x.grid(column=0,row=1)

    # x^2 button
    btn_x2 = tk.Button(root,text='x^2',command=powNum)
    btn_x2.grid(column=1,row=1)

    # x^3 button 
    btn_x3 = tk.Button(root,text='x^3',command=powThreeNum)
    btn_x3.grid(column=2,row=1)

    # y^x button
    btn_yx = tk.Button(root,text='y^x',command=lambda: press('**'))
    btn_yx.grid(column=3,row=1)

    # C button
    btn_c = tk.Button(root,text='C',command=clear)
    btn_c.grid(column=4,row=1)

    # +/- button 
    btn_plusminus = tk.Button(root,text='+/-',command= posNegNum)
    btn_plusminus.grid(column=5,row=1)

    # dividing button
    btn_div = tk.Button(root,text='÷',command=lambda: press('/'))
    btn_div.grid(column=6,row=1)

    # X button
    btn_x = tk.Button(root,text='x',command=lambda: press('*'))
    btn_x.grid(column=7, row=1) 

    # X! button
    btn_x1 = tk.Button(root,text='x!',command=factorialNum)
    btn_x1.grid(column=0,row=2)

    # square root button
    btn_square = tk.Button(root,text='√',command=squareNum)
    btn_square.grid(column=1,row=2)

    # % button
    btn_per = tk.Button(root,text='%',command=percentageNum)
    btn_per.grid(column=2,row=2)

    # log button
    btn_log = tk.Button(root,text='log',command=logNum)
    btn_log.grid(column=3,row=2)

    # 7 button
    btn_7 = tk.Button(root,text='7',command=lambda: press(7))
    btn_7.grid(column=4,row=2)

    # 8 button
    btn_8 = tk.Button(root,text='8',command=lambda: press(8))
    btn_8.grid(column=5,row=2)

    # 9 button
    btn_9 = tk.Button(root,text='9',command=lambda: press(9))
    btn_9.grid(column=6,row=2)

    # minus button
    btn_minus = tk.Button(root,text='-',command=lambda: press('-'))
    btn_minus.grid(column=7,row=2)

    # sin button 
    btn_sin = tk.Button(root,text='sin',command=sinNum)
    btn_sin.grid(column=0,row=3)

    # cos button 
    btn_cos = tk.Button(root,text='cos',command=cosNum)
    btn_cos.grid(column=1,row=3)

    # tan button 
    btn_tan = tk.Button(root,text='tan',command=tanNum)
    btn_tan.grid(column=2,row=3)

    # ln button 
    btn_ln = tk.Button(root,text='ln',command=lnNum)
    btn_ln.grid(column=3,row=3)

    # 4 button
    btn_4 = tk.Button(root,text='4',command=lambda: press(4))
    btn_4.grid(column=4,row=3)

    # 5 button
    btn_5 = tk.Button(root,text='5',command=lambda: press(5))
    btn_5.grid(column=5,row=3)

    # 6 button
    btn_6 = tk.Button(root,text='6',command=lambda: press(6))
    btn_6.grid(column=6,row=3)

    # + button
    btn_plus = tk.Button(root,text='+',command=lambda: press('+'))
    btn_plus.grid(column=7,row=3)

    # sinh button
    btn_sinh = tk.Button(root,text='sinh',command=sinhNum)
    btn_sinh.grid(column=0,row=4)

    # cosh button
    btn_cosh = tk.Button(root,text='cosh',command=coshNum)
    btn_cosh.grid(column=1,row=4)

    # tanh button
    btn_tanh = tk.Button(root,text='tanh',command=tanhNum)
    btn_tanh.grid(column=2,row=4)

    # eX button
    btn_ex = tk.Button(root,text='eX',command=exNum)
    btn_ex.grid(column=3,row=4)

    # 1 button
    btn_1 = tk.Button(root,text='1',command=lambda: press(1))
    btn_1.grid(column=4,row=4)

    # 2 button
    btn_2 = tk.Button(root,text='2',command=lambda: press(2))
    btn_2.grid(column=5,row=4)

    # 3 button
    btn_3 = tk.Button(root, text='3',command=lambda: press(3))
    btn_3.grid(column=6,row=4)

    # = button
    btn_equals = tk.Button(root,text='=',command=equalpress)
    btn_equals.grid(column=7,row=4,rowspan=5)

    # aesthetic button
    btn_1st = tk.Button(root,text='')
    btn_1st.grid(column=0,row=5)

    # pi button
    btn_pi = tk.Button(root,text='π',command=lambda: press(math.pi))
    btn_pi.grid(column=1,row=5)

    # aesthetic button
    btn_ee = tk.Button(root,text='')
    btn_ee.grid(column=2,row=5)

    # rnd button
    btn_rnd = tk.Button(root,text='rnd',command=lambda: press(1/(random.randint(1,10000))))
    btn_rnd.grid(column=3,row=5)

    # 0 button
    btn_0 = tk.Button(root,text='0',command=lambda: press(0))
    btn_0.grid(column=4,columnspan=2,row=5)

    # dot button
    btn_dot = tk.Button(root,text='.',command=lambda: press('.'))
    btn_dot.grid(column=6,row=5)


    # end of Loop
    root.mainloop()