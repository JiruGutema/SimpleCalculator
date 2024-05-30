#this simple project is from jiregna gutema
#this is my first way to the coding world
from tkinter import *

jiren = Tk()

jiren.configure(background='gray')
jiren.title("jiru's calc")
jiren.geometry('200x300')
jiren.resizable(False,False)
calc = Label(jiren, font=('', 15), text="calc. executer")
calc.pack(fill=None, side="top",expand=True)

result=Label(jiren,  font=('', 15), text="", width=90)
result.pack(fill=NONE, side="top", pady=5, expand=True)

def number(num):
    prev = result.cget('text')
    final = prev + str(num)
    result.configure(text=final)
def equalto():
    expr = result.cget('text')
    result.configure(text=str(eval(expr)))
def reset():
    result.configure(text='')


frame1 = Frame(jiren)
frame1.pack(side='left',padx=5)
frame2 = Frame(jiren)
frame2.pack(side='left',padx=5)
frame3 = Frame(jiren)
frame3.pack(side='left',padx=5)
frame4 = Frame(jiren)
frame4.pack(side='left',padx=5)

btn1 = Button(frame1, background='#770011', font=('', 15), text="1", command=lambda : number(1)).pack(side="top", pady=5)
btn4 = Button(frame1, background='#770011', font=('', 15), text="4", command=lambda : number(4)).pack(side="top", pady=5)
btn7 = Button(frame1, background='#770011', font=('', 15), text="7", command=lambda : number(7)).pack(side="top", pady=5)
btndo = Button(frame1, background='#770011', font=('', 15), text=".", command=lambda : number('.')).pack(side="top", pady=5)

btn2 = Button(frame2, background='#770011', font=('', 15), text="2", command=lambda : number(2)).pack(side="top", pady=5)
btn5 = Button(frame2, background='#770011', font=('', 15), text="5", command=lambda : number(5)).pack(side="top", pady=5)
btn8 = Button(frame2, background='#770011', font=('', 15), text="8", command=lambda : number(8)).pack(side="top", pady=5)
btn0 = Button(frame2, background='#770011', font=('', 15), text="0", command=lambda : number(0)).pack(side="top", pady=5)

btn3 = Button(frame3, background='#770011', font=('', 15), text="3", command=lambda : number(3)).pack(side="top", pady=5)
btn6 = Button(frame3, background='#770011', font=('', 15), text="6", command=lambda : number(6)).pack(side="top", pady=5)
btn9 = Button(frame3, background='#770011', font=('', 15), text="9", command=lambda : number(9)).pack(side="top", pady=5)
btnde = Button(frame3, background='#770011', font=('', 15), text="c", command=reset).pack(side="top", pady=5)

btnm = Button(frame4, background='#777777', font=('', 14), text="*", command=lambda : number('*')).pack(side="top", pady=1)
btnd = Button(frame4, background='#770011', font=('', 14), text="/", command=lambda : number('/')).pack(side="top", pady=1)
btns = Button(frame4, background='#770011', font=('', 14), text="-", command=lambda : number('-')).pack(side="top", pady=1)
btnp = Button(frame4, background='#770011', font=('', 14), text="+", command=lambda : number('+')).pack(side="top", pady=1)
btne = Button(frame4, background='#770011', font=('', 14), text="=", command=equalto).pack(side="top", pady=1)


jiren.mainloop()


