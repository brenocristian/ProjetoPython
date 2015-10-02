from tkinter import *

app = Tk()
app.title("Janela em Python")
app.geometry('600x500+900+900')

quantsim = IntVar()
quantsim.set(0)
quantnao = IntVar()
quantnao.set(0)

def apertou01():
    quantsim.set(quantsim.get() + 1)

def apertou02():
    quantnao.set(quantnao.get() + 1)

rotulo = Label(app, text = 'Faça sua escolha')
rotulo.pack(pady = 60)

lab1 = Label(app, textvariable = quantsim )
lab1.pack(side = "left")

lab2 = Label(app, textvariable = quantnao )
lab2.pack(side = "right")

b1 = Button (app, text = "sim", width = 10, command = apertou01)
b1.pack(side ="left", padx = 10 , pady = 10)

b2 = Button (app, text = "não", width = 10, command = apertou02)
b2.pack(side ="right", padx = 10 , pady = 10)

app.mainloop ()
