import math
import tkinter as tk
try:  # Python-2
    from tkinter import *
    import tkFont
except ImportError:  # Python-3
    from tkinter import *
    from tkinter import font as tkFont



root = tk.Tk()
root.title("Calculator")
root.resizable('0','0')
#root.iconbitmap('D:\python\calculator\calculator.ico')
enter = tk.Entry(root, width=25, font=("Arial", 20), bg="#ececec", fg="#5b5b5b", justify= 'right' )
enter.grid(row=0, column=0, columnspan=4,)
enter1 = tk.Entry( root, width=13, font=("Arial", 40), bg="White", fg="Black", justify= "right" )
enter1.grid(row=1, column=0, pady = 3, columnspan=4)
root.count = 0
root.count1 =0


#functions

def click():
    root.count = root.count +1
    root.count1 = root.count1 +1

def onclick(num):
    enter.insert(root.count , num )

def onclick_(no):
    
    enter1.insert(root.count1,no)
    enter.insert(root.count , no )

def onclick_decimal(dec):
    enter.insert(root.count,dec)

def clr():
    enter1.delete(0, tk.END)
    enter.delete(0, tk.END)

def backspace():
    enter.delete(enter.index(tk.END)-1)
    enter1.delete(0)

def addition():
    no1 = enter1.get()
    global first
    global operation
    operation = "add"
    first= int(no1)
    enter1.delete(0,tk.END)

def subtract():
    no1 = enter1.get()
    global first
    global operation
    operation = "subt"
    first= int(no1)
    enter1.delete(0,tk.END)
    

def multiply():
    no1 = enter1.get()
    global first
    global operation
    operation = "mul"
    first= int(no1)
    enter1.delete(0,tk.END)
    

def devide():
    no1 = enter1.get()
    global first
    global operation
    operation = "dev"
    first= int(no1)
    enter1.delete(0,tk.END)
    

def sqt():
    rootof = int(enter.get())
    value = math.sqrt(rootof)
    enter.delete(0,tk.END)
    enter1.delete(0,tk.END)
    enter.insert(0,value)
    enter1.insert(0,value)


def sqr():
    squareof = int(enter.get())
    value = squareof*squareof
    enter1.delete(0, tk.END)
    enter.delete(0,tk.END)
    enter.insert(0,value)
    enter1.insert(0,value)

def sine():
    root.count = root.count +2
    enter.insert(root.count,"Sin")
    global operation
    operation = "sin"
    
def cosine():
    root.count = root.count +2
    enter.insert(root.count,"Cos")
    global operation
    operation = "cos"
    

def tangent():
    root.count = root.count +2
    enter.insert(root.count,"Tan")
    global operation
    operation = "tan"
    
    
  
def calculate():
    secondnum = enter1.get()
    root.count1=0
    global no2 
    no2 = int(secondnum)
    enter.delete(0,tk.END)
    enter1.delete(0,tk.END)
    
    if operation =="add":
        enter.insert(0, first+ no2)
        enter1.insert(0, first+ no2)
    elif operation =="subt":
        enter.insert(0, first- no2)
        enter1.insert(0, first- no2)
    elif operation =="mul":
        enter.insert(0, first* no2)
        enter1.insert(0, first* no2)
    elif operation =="dev":
        enter.insert(0, first/ no2)
        enter1.insert(0, first/ no2)
    elif operation =="cos":
        no2 = float(no2/180)
        value = math.cos(math.pi*( no2))
        value = round(value,2)        
        enter1.insert(0,value)
    elif operation =="sin":
        no2 = float(no2/180)
        value = math.sin(math.pi*( no2))
        value = round(value,2)        
        enter1.insert(0,value)
    elif operation =="tan":
        no2 = float(no2/180)
        value = math.tan(math.pi*( no2))
        value = round(value,2)        
        enter1.insert(0,value)


#buttons

helv15 = tkFont.Font(family='Helvetica', size=15, weight=tkFont.BOLD)
helv12 = tkFont.Font(family='Helvetica', size=12, weight=tkFont.BOLD)



square = tk.Button(root, text="x"+ u'\u00b2', font=helv15, padx="33", pady="15", bg="#a4a0a0" , command= lambda:[sqr()]).grid(row=2, column=0)
sroot = tk.Button(root, text=u'\u221a' + "x",font=helv15, padx="35", pady="15", bg="#a4a0a0" , command=lambda:sqt()).grid(row=2, column=1)
clear = tk.Button(root, text="C", padx="35",font=helv15, pady="15", bg="#a4a0a0" , command= lambda: clr()).grid(row=2, column=2)
back = tk.Button(root, text=u"\u2b88",font=helv15, padx="35", bg="#a4a0a0" , pady="15", command= lambda: [backspace()]).grid(row=2, column=3)

sin = tk.Button(root, text="Sin",font=helv12, padx="30", pady="20",bg="#ddd3d3", command=lambda: [sine(), click()])
sin.grid(row=3, column=0)
cos = tk.Button(root, text="Cos",font=helv12, padx="28", pady="20",bg="#ddd3d3", command=lambda: [cosine(), click()])
cos.grid(row=3, column=1)
tan = tk.Button(root, text="Tan",font=helv12, padx="28", pady="20",bg="#ddd3d3", command= lambda:[tangent(), click()])
tan.grid(row=3, column=2)
add = tk.Button(root, text="+",font=helv15, padx="35", pady="17",bg="#ddd3d3",command=lambda: [onclick('+'), click(),addition()]).grid(row=3, column=3)

num7 = tk.Button(root, text="7",font=helv15, padx="35", pady="20", command=lambda: [onclick_(7), click()]).grid(row=4, column=0)
num8 = tk.Button(root, text="8",font=helv15, padx="35", pady="20",command=lambda: [onclick_(8), click()]).grid(row=4, column=1)
num9 = tk.Button(root, text="9",font=helv15, padx="35", pady="20",command=lambda: [onclick_(9), click()]).grid(row=4, column=2)
sub = tk.Button(root, text="-",font=helv15, padx="38", pady="20",bg="#ddd3d3",command=lambda: [onclick('-'), click(), subtract(), calculate()]).grid(row=4, column=3)

num4 = tk.Button(root, text="4",font=helv15, padx="35", pady="20", command=lambda: [onclick_(4), click()]).grid(row=5, column=0)
num5 = tk.Button(root, text="5",font=helv15, padx="35", pady="20", command=lambda: [onclick_(5), click()]).grid(row=5, column=1)
num6 = tk.Button(root, text="6",font=helv15, padx="35", pady="20", command=lambda: [onclick_(6), click()]).grid(row=5, column=2)
multi = tk.Button(root,  padx="35",font=helv15, pady="20",text=u'\u00d7',bg="#ddd3d3",command=lambda: [onclick(u'\u00d7'), click(),multiply(), calculate()]).grid(row=5, column=3)

num1 = tk.Button(root, text="1",font=helv15, padx="35", pady="20", command=lambda: [onclick_(1), click()]).grid(row=6, column=0)
num2 = tk.Button(root, text="2",font=helv15, padx="35", pady="20", command=lambda: [onclick_(2), click()]).grid(row=6, column=1) 
num3 = tk.Button(root, text="3",font=helv15, padx="35", pady="20", command=lambda: [onclick_(3), click()]).grid(row=6, column=2)
div = tk.Button(root, text=u"\u00f7",font=helv15, padx="35", pady="20",bg="#ddd3d3", command=lambda: [onclick(u'\u00f7'), click(),devide(), calculate()]).grid(row=6, column=3)


zero = tk.Button(root, text="0",font=helv15, padx="35", pady="20", command=lambda: [onclick_('0'), click()]).grid(row=7, column=1)
point = tk.Button(root, text=".",font=helv15, padx="35", pady="20", command=lambda: [onclick_decimal('.'), click()]).grid(row=7, column=0)
equal = tk.Button(root, text="=",font=helv15,width=10, padx="35", pady="20", bg="#a4a0a0" ,command=lambda: calculate()).grid(row=7, column=2, columnspan=2)

root.mainloop()
