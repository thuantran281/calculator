import tkinter as tk
from tkinter import *

# instantiate the windows
calculator = tk.Tk()
calculator.title('Mini Calculator')
calculator.geometry('395x400')

calc = Entry(calculator, width=62, borderwidth=4)
calc.grid(columnspan=16, padx=4, pady=10)

def resetValue():
    calc.delete(0, END)

def addingButton(n):
    # calc.delete(0, END)
    current = calc.get()
    calc.delete(0, END)
    calc.insert(0, str(current) + str(n))

def add():
    first = calc.get()
    global firstNumber
    global math
    math = 'Addition'
    firstNumber = float(first)
    calc.delete(0, END)

def subtract():
    first = calc.get()
    global firstNumber
    global math
    math = 'Subtraction'
    firstNumber = float(first)
    calc.delete(0, END)

def multiply():
    first = calc.get()
    global firstNumber
    global math
    math = 'Multiplication'
    firstNumber = float(first)
    calc.delete(0, END)

def division():
    first = calc.get()
    global firstNumber
    global math
    math = 'Subtraction'
    firstNumber = float(first)
    calc.delete(0, END)

def equal():
    secondNumber = calc.get()
    calc.delete(0, END)

    if math == 'Addition':
        calc.insert(0, firstNumber + float(secondNumber))
    if math == 'Subtraction':
        calc.insert(0, firstNumber - float(secondNumber))
    if math == 'Multiplication':
        calc.insert(0, firstNumber * float(secondNumber))
    if math == 'Division':
        calc.insert(0, firstNumber / float(secondNumber))

    

# instantiate buttons

zero = Button(calculator, text='0', padx=40, pady=15, command=lambda: addingButton(0))
zero.grid(row=4, column=2)

buttonOne = Button(calculator, text='1', padx=40, pady=15,
                       command=lambda: addingButton(1))
buttonOne.grid(row=3, column=2)

buttonTwo = Button(calculator, text='2', padx=40, pady=15,
                       command=lambda: addingButton(2))
buttonTwo.grid(row=3, column=3)

buttonThree = Button(calculator, text='3', padx=40, pady=15,
                         command=lambda: addingButton(3))
buttonThree.grid(row=3, column=4)

buttonFour = Button(calculator, text='4', padx=40, pady=15,
                        command=lambda: addingButton(4))
buttonFour.grid(row=2, column=2)

buttonFive = Button(calculator, text='5', padx=40, pady=15,
                        command=lambda: addingButton(5))
buttonFive.grid(row=2, column=3)

buttonSix = Button(calculator, text='6', padx=40, pady=15,
                       command=lambda: addingButton(6))
buttonSix.grid(row=2, column=4)

buttonSeven = Button(calculator, text='7', padx=40, pady=15,
                         command=lambda: addingButton(7))
buttonSeven.grid(row=1, column=2)

buttonEight = Button(calculator, text='8', padx=40, pady=15,
                         command=lambda: addingButton(8))
buttonEight.grid(row=1, column=3)

buttonNine = Button(calculator, text='9', padx=40, pady=15,
                        command=lambda: addingButton(9))
buttonNine.grid(row=1, column=4)

comma = Button(calculator, text='.', padx=41, pady=15, 
                        command=lambda: addingButton("."))
comma.grid(row=4, column=3)

clear = Button(calculator, text='C', padx=39, pady=15, 
                        command=resetValue)
clear.grid(row=4, column=4)

divButton = Button(calculator, text='/', padx=40, pady=15, 
                        command=division)
divButton.grid(row=4, column=5)

multiplyButton = Button(calculator, text='x', padx=41, pady=15, 
                        command=multiply)
multiplyButton.grid(row=3, column=5)

subtractButton = Button(calculator, text='-', padx=41, pady=15, 
                        command=subtract)
subtractButton.grid(row=2, column=5)

plusButton = Button(calculator, text='+', padx=40, pady=15, 
                        command=add)
plusButton.grid(row=1, column=5)

equalButton = Button(calculator, text='=', padx=39, pady=15, 
                        command=equal)
equalButton.grid(row=5, column=4)

calc.mainloop()

#--------------------------------------------------------------------------------------------
# This code was adapted and modified from the original version
# of Codemy, given is the link 
# https://www.youtube.com/watch?v=oq3lJdhnPp8&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=7
