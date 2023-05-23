from tkinter import *
from tkmacosx import Button
from math import *

#Conf Ventana
ventana = Tk()
ventana.title("Calculadora")
ventana.geometry("260x390")
ventana.configure(background="gray15")
ventana.resizable(False,False)

#Variables
mostrar_cero = True
input_text=StringVar()
input_text.set("0")
operador=""

#Funciones
def btnClick(num):
    global operador, mostrar_cero
    if mostrar_cero:
        mostrar_cero = False
    operador = operador + str(num)
    input_text.set(operador)

def operacion():
    global operador, mostrar_cero
    try:
        opera=eval(operador)
    except:
        clear()
        opera=("Syntax Error")
    input_text.set(opera)
    mostrar_cero = True

def porcentaje():
    global operador, mostrar_cero
    opera=eval(str(float(operador)/100))
    input_text.set(opera)
    mostrar_cero = True

def raiz():
    global operador, mostrar_cero
    opera=eval(str(float(operador)**0.5))
    input_text.set(opera)
    mostrar_cero = True

def clear():
    global operador
    operador=("")
    input_text.set("0")

def cero_pantalla():
    label=Label(ventana, text="0", font=('arial', 45), width=1, bg="gray15", justify="right").place(x=215,y=15)


#Conf Botones
ancho_boton_but=120
alto_boton_but=60
ancho_boton_top=60
alto_boton_top=60
color_boton1=('azure4')
color_boton2=('ORANGE')

#Botones
Boton0=Button(ventana, command=lambda:btnClick(0), font=('arial', 20), text="0", fg='WHITE', activebackground='GRAY85', focuscolor='WHITE', focusthickness=0, borderless=True, bg=color_boton1, width=ancho_boton_but, height=alto_boton_but).place(x=10, y=315)
Boton1=Button(ventana, command=lambda:btnClick(1), font=('arial', 20), text="1", fg='WHITE', activebackground='GRAY85', focuscolor='WHITE', focusthickness=0, borderless=True, highlightthickness=0, bg=color_boton1, width=ancho_boton_top, height=alto_boton_top).place(x=10, y=255)
Boton2=Button(ventana, command=lambda:btnClick(2), font=('arial', 20), text="2", fg='WHITE', activebackground='GRAY85', focuscolor='WHITE', focusthickness=0, borderless=True, highlightthickness=0, bg=color_boton1, width=ancho_boton_top, height=alto_boton_top).place(x=70, y=255)
Boton3=Button(ventana, command=lambda:btnClick(3), font=('arial', 20), text="3", fg='WHITE', activebackground='GRAY85', focuscolor='WHITE', focusthickness=0, borderless=True, highlightthickness=0, bg=color_boton1, width=ancho_boton_top, height=alto_boton_top).place(x=130, y=255)
Boton4=Button(ventana, command=lambda:btnClick(4), font=('arial', 20), text="4", fg='WHITE', activebackground='GRAY85', focuscolor='WHITE', focusthickness=0, borderless=True, highlightthickness=0, bg=color_boton1, width=ancho_boton_top, height=alto_boton_top).place(x=10, y=195)
Boton5=Button(ventana, command=lambda:btnClick(5), font=('arial', 20), text="5", fg='WHITE', activebackground='GRAY85', focuscolor='WHITE', focusthickness=0, borderless=True, highlightthickness=0, bg=color_boton1, width=ancho_boton_top, height=alto_boton_top).place(x=70, y=195)
Boton6=Button(ventana, command=lambda:btnClick(6), font=('arial', 20), text="6", fg='WHITE', activebackground='GRAY85', focuscolor='WHITE', focusthickness=0, borderless=True, highlightthickness=0, bg=color_boton1, width=ancho_boton_top, height=alto_boton_top).place(x=130, y=195)
Boton7=Button(ventana, command=lambda:btnClick(7), font=('arial', 20), text="7", fg='WHITE', activebackground='GRAY85', focuscolor='WHITE', focusthickness=0, borderless=True, highlightthickness=0, bg=color_boton1, width=ancho_boton_top, height=alto_boton_top).place(x=10, y=135)
Boton8=Button(ventana, command=lambda:btnClick(8), font=('arial', 20), text="8", fg='WHITE', activebackground='GRAY85', focuscolor='WHITE', focusthickness=0, borderless=True, highlightthickness=0, bg=color_boton1, width=ancho_boton_top, height=alto_boton_top).place(x=70, y=135)
Boton9=Button(ventana, command=lambda:btnClick(9), font=('arial', 20), text="9", fg='WHITE', activebackground='GRAY85', focuscolor='WHITE', focusthickness=0, borderless=True, highlightthickness=0, bg=color_boton1, width=ancho_boton_top, height=alto_boton_top).place(x=130, y=135)
BotonC=Button(ventana, command=clear, font=('arial', 20), text="C", fg='WHITE', activebackground='GRAY85', focuscolor='WHITE', focusthickness=0, borderless=True, highlightthickness=0, bg='GRAY35', width=ancho_boton_top, height=alto_boton_top).place(x=10, y=75)
BotonSqrt=Button(ventana, command=raiz, font=('arial', 20), text="√", fg='WHITE', activebackground='GRAY85', focuscolor='WHITE', focusthickness=0, borderless=True, highlightthickness=0, bg='GRAY35', width=ancho_boton_top, height=alto_boton_top).place(x=70, y=75)
BotonPorcentaje=Button(ventana, command=porcentaje, font=('arial', 20), text="%", fg='WHITE', activebackground='GRAY85', focuscolor='WHITE', focusthickness=0, borderless=True, highlightthickness=0, bg='GRAY35', width=ancho_boton_top, height=alto_boton_top).place(x=130, y=75)
BotonDiv=Button(ventana, command=lambda:btnClick("/"), font=('arial', 20), text="÷", fg='WHITE', activebackground=color_boton2, focuscolor='GRAY10', focusthickness=2, borderless=True, highlightthickness=0, bg=color_boton2, width=ancho_boton_top, height=alto_boton_top).place(x=190, y=75)
BotonMult=Button(ventana, command=lambda:btnClick("*"), font=('arial', 20), text="x", fg='WHITE', activebackground=color_boton2, focuscolor='GRAY10', focusthickness=2, borderless=True, highlightthickness=0, bg=color_boton2, width=ancho_boton_top, height=alto_boton_top).place(x=190, y=135)
BotonMenos=Button(ventana, command=lambda:btnClick("-"), font=('arial', 20), text="-", fg='WHITE', activebackground=color_boton2, focuscolor='GRAY10', focusthickness=2, borderless=True, highlightthickness=0, bg=color_boton2, width=ancho_boton_top, height=alto_boton_top).place(x=190, y=195)
BotonMas=Button(ventana, command=lambda:btnClick("+"), font=('arial', 20), text="+", fg='WHITE', activebackground=color_boton2, focuscolor='GRAY10', focusthickness=2, borderless=True, highlightthickness=0, bg=color_boton2, width=ancho_boton_top, height=alto_boton_top).place(x=190, y=255)
BotonIgual=Button(ventana, command=operacion, font=('arial', 20), text="=", fg='WHITE', activebackground=color_boton2, focuscolor='GRAY10', focusthickness=2, borderless=True, highlightthickness=0, bg=color_boton2, width=ancho_boton_top, height=alto_boton_top).place(x=190, y=315)
BotonComa=Button(ventana, command=lambda:btnClick("."), font=('arial', 20), text=",", fg='WHITE', activebackground='GRAY85', focuscolor='WHITE', focusthickness=0, borderless=True, highlightthickness=0, bg=color_boton1, width=ancho_boton_top, height=alto_boton_top).place(x=130, y=315)

#Pantalla
salida = Entry(ventana, font=('arial', 45), textvariable=input_text, width=9, bd=0, borderwidth=0,
               highlightbackground="gray15", highlightcolor="gray15", insertwidth=0, bg="gray15", justify="right")
salida.place(x=10, y=15)

ventana.mainloop()