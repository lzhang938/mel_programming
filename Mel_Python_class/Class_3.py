from tkinter import *
expression=""
def press(num):
    global expression
    expression=expression+str(num)
    equation.set(expression)
def evaluate():
    global expression
    total=eval(expression)
    equation.set(str(total))
    expression=""
def clearexpression():
    global expression
    expression=""
    equation.set(expression)

window=Tk()
window.config(bg="yellow")
window.title("Calculator")
window.geometry("300x200")
equation=StringVar()
expression_field=Entry(window, textvariable=equation, )
expression_field.grid(columnspan=4, ipadx=70)

equation.set("Please enter your expression")

button1=Button(window, text=" 1 ", height=1, width=8, command=lambda: press(1))
button1.grid(row=2, column=0)
button2=Button(window, text=" 2 ", height=1, width=8, command=lambda: press(2))
button2.grid(row=2, column=1)
button3=Button(window, text=" 3 ", height=1, width=8, command=lambda: press(3))
button3.grid(row=2, column=2)
plus=Button(window, text=" + ", height=1, width=8, command=lambda: press("+"))
plus.grid(row=2, column=3)

button4=Button(window, text=" 4 ", height=1, width=8, command=lambda: press(4))
button4.grid(row=3, column=0)
button5=Button(window, text=" 5 ", height=1, width=8, command=lambda: press(5))
button5.grid(row=3, column=1)
button6=Button(window, text=" 6 ", height=1, width=8, command=lambda: press(6))
button6.grid(row=3, column=2)
minus=Button(window, text=" - ", height=1, width=8, command=lambda: press("-"))
minus.grid(row=3, column=3)

button7=Button(window, text=" 7 ", height=1, width=8, command=lambda: press(7))
button7.grid(row=4, column=0)
button8=Button(window, text=" 8 ", height=1, width=8, command=lambda: press(8))
button8.grid(row=4, column=1)
button9=Button(window, text=" 9 ", height=1, width=8, command=lambda: press(9))
button9.grid(row=4, column=2)
multiply=Button(window, text="*", height=1, width=8, command=lambda: press("*"))
multiply.grid(row=4, column=3)

button0=Button(window, text=" 0 ", height=1, width=8, command=lambda: press(0))
button0.grid(row=5, column=1)
equals=Button(window, text=" = ", height=1, width=8, command=evaluate)
equals.grid(row=5, column=2)
clear=Button(window, text=" clear ", height=1, width=8)
clear.grid(row=5, column=0)
divide=Button(window, text=" / ", height=1, width=8, command=lambda: press("/"))
divide.grid(row=5, column=3)
window.mainloop()