#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


class Calculadora():

    def __init__(self, operando1, operando2):
        self.operando1 = operando1
        self.operando2 = operando2

    def suma(self):
        return self.operando1 + self.operando2

    def resta(self):
        return self.operando1 - self.operando2


class CalculadoraHija(Calculadora):

    def mult(self):
        return self.operando1 * self.operando2

    def div(self):
        return self.operando1 / self.operando2


if __name__ == "__main__":

    fichero = open(sys.argv[1], "r")
    lineas = fichero.readlines()
    numero = len(lineas)
    x = 0
    while x < numero:
        linea = lineas[x][:-1]
        lista_palabras = linea.split(",")
        if lista_palabras[0] == "suma":
            acumulador = float(lista_palabras[1])
            y = 2
            while y < len(lista_palabras):
                operandos = Calculadora(acumulador,float(lista_palabras[y]))
                acumulador = operandos.suma()
                y = y+1
            print(acumulador)
        if lista_palabras[0] == "resta":
            acumulador = float(lista_palabras[1])
            y = 2
            while y < len(lista_palabras):
                operandos = Calculadora(acumulador,float(lista_palabras[y]))
                acumulador = operandos.resta()
                y = y+1
            print(acumulador)
        if lista_palabras[0] == "multiplica":
            acumulador = float(lista_palabras[1])
            y = 2
            while y < len(lista_palabras):
                operandos = CalculadoraHija(acumulador,float(lista_palabras[y]))
                acumulador = operandos.mult()
                y = y+1
            print(acumulador)
        if lista_palabras[0] == "divide":
            acumulador = float(lista_palabras[1])
            y = 2
            while y < len(lista_palabras):
                operandos = CalculadoraHija(acumulador,float(lista_palabras[y]))
                try:
                    acumulador = operandos.div()
                except ZeroDivisionError:
                    sys.exit("Error: Division by zero is not allowed")
                y = y+1
            print(acumulador)                                                                      
        x = x+1
    

    
