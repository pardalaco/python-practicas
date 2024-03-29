#!/usr/bin/python3
# -*- coding: utf-8 -*-

from tkinter import *

raiz=Tk()

miFrame=Frame(raiz)

miFrame.pack()

operacion=""

resultado=0

#---------------Pantalla-------------------

numeroPantalla=StringVar()

pantalla=Entry(miFrame, textvariable=numeroPantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(background="black", fg="#64B5F6", justify="right")


#---------------Pulsaciones Teclado-------------

def numeroPulsado(num):

	global operacion

	if operacion!="": # Aqui estamos preguntando si la variable operacion es diferente a ""

		numeroPantalla.set(num) # Le estamos diciendo que en el caso de que el usuario haya pulsado el boton suma no concatene con el siguiente número

		operacion="" # Estamos volviendo a poner que operación valga "" como al principio

	else:

#		numeroPantalla.set("4") # En estos momentos la función solo escribe un 4 y si pulsamos otra vez es como si el numero se estubiera reescribiendo

		numeroPantalla.set(numeroPantalla.get() + num) # Con la función `get` lo que hacemos es decir que lea todo lo que hay en pantalla y que añada el 4

#--------------Función suma------------------

def suma(num): # Cuando apriean el boton de sumar se hace una llamada a la variable operacion y almacena dentro de la variable global operacion la palabra suma

	global operacion

	global resultado

	resultado+=float(num) # Incrementa a la variable resultado el valor numérico entero que pudiera haber en pantalla

	operacion="suma"

	numeroPantalla.set(resultado)

#--------------Función resta------------------

def resta(num): # Cuando apriean el boton de sumar se hace una llamada a la variable operacion y almacena dentro de la variable global operacion la palabra resta

	global operacion

	global resultado

	resultado-=float(num) # Incrementa a la variable resultado el valor numérico entero que pudiera haber en pantalla

	operacion="resta"

	numeroPantalla.set(resultado)

#--------------Función multiplicación------------------

def multi(num): # Cuando apriean el boton de sumar se hace una llamada a la variable operacion y almacena dentro de la variable global operacion la palabra multi

	global operacion

	global resultado

	resultado*(float(num)) # Incrementa a la variable resultado el valor numérico entero que pudiera haber en pantalla

	operacion="multi"

	numeroPantalla.set(resultado)

#--------------Función división------------------

def divi(num): # Cuando apriean el boton de sumar se hace una llamada a la variable operacion y almacena dentro de la variable global operacion la palabra divi

	global operacion

	global resultado

	resultado/=float(num) # Incrementa a la variable resultado el valor numérico entero que pudiera haber en pantalla

	operacion="multi"

	numeroPantalla.set(resultado)

#---------------Funcion el_resultado--------

def el_resultado():

	global resultado

	numeroPantalla.set(resultado+float(numeroPantalla.get()))

	resultado=0

#---------------Fila 1----------------------

boton7=Button(miFrame, text="7", width=3, command=lambda:numeroPulsado("7"))# Comand sirve para ejecutar una funcion externa
boton7.grid(row=2, column=1)
boton8=Button(miFrame, text="8", width=3, command=lambda:numeroPulsado("8"))
boton8.grid(row=2, column=2)
boton9=Button(miFrame, text="9", width=3, command=lambda:numeroPulsado("9"))
boton9.grid(row=2, column=3)
botonDivi=Button(miFrame, text="/", width=3, command=lambda:numeroPulsado("/"))
botonDivi.grid(row=2, column=4)

#---------------Fila 2----------------------

boton4=Button(miFrame, text="4", width=3, command=lambda:numeroPulsado("4"))# En python al utilizar los parentesis estamos ejecutando la funicon, por lo tanto estamos ejecutando command // la funcion lambda nos permita que cuando haya parentesis no se ejecute directamente y se espere a cuando le toque ejecutarse
boton4.grid(row=3, column=1)
boton5=Button(miFrame, text="5", width=3, command=lambda:numeroPulsado("5"))
boton5.grid(row=3, column=2)
boton6=Button(miFrame, text="6", width=3, command=lambda:numeroPulsado("6"))
boton6.grid(row=3, column=3)
#botonMul=Button(miFrame, text="x", width=3, command=lambda:numeroPulsado("x"))
botonMul=Button(miFrame, text="x", width=3, command=lambda:suma(numeroPantalla.get()))
botonMul.grid(row=3, column=4)

#---------------Fila 3----------------------

boton1=Button(miFrame, text="1", width=3, command=lambda:numeroPulsado("1"))
boton1.grid(row=4, column=1)
boton2=Button(miFrame, text="2", width=3, command=lambda:numeroPulsado("2"))
boton2.grid(row=4, column=2)
boton3=Button(miFrame, text="3", width=3, command=lambda:numeroPulsado("3"))
boton3.grid(row=4, column=3)
#botonRes=Button(miFrame, text="-", width=3, command=lambda:numeroPulsado("-"))
botonRes=Button(miFrame, text="-", width=3, command=lambda:resta(numeroPantalla.get()))
botonRes.grid(row=4, column=4)

#---------------Fila 4----------------------

boton0=Button(miFrame, text="0", width=3, command=lambda:numeroPulsado("0"))
boton0.grid(row=5, column=1)
botonIgual=Button(miFrame, text="=", width=3, command=lambda:el_resultado())
botonIgual.grid(row=5, column=2)
botonComa=Button(miFrame, text=",", width=3, command=lambda:numeroPulsado(","))
botonComa.grid(row=5, column=3)
botonSum=Button(miFrame, text="+", width=3, command=lambda:suma(numeroPantalla.get()))
botonSum.grid(row=5, column=4)


raiz.mainloop()