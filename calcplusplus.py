#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import csv


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

    with open(sys.argv[1], "r") as fichero:
        lista = csv.reader(fichero)
        for linea in lista:
            if linea[0] == "suma":
                acumulador = float(linea[1])
                y = 2
                while y < len(linea):
                    operandos = Calculadora(acumulador, float(linea[y]))
                    acumulador = operandos.suma()
                    y = y+1
                print(acumulador)
            elif linea[0] == "resta":
                acumulador = float(linea[1])
                y = 2
                while y < len(linea):
                    operandos = Calculadora(acumulador, float(linea[y]))
                    acumulador = operandos.resta()
                    y = y+1
                print(acumulador)
            elif linea[0] == "multiplica":
                acumulador = float(linea[1])
                y = 2
                while y < len(linea):
                    operandos = CalculadoraHija(acumulador, float(linea[y]))
                    acumulador = operandos.mult()
                    y = y+1
                print(acumulador)
            elif linea[0] == "divide":
                acumulador = float(linea[1])
                y = 2
                while y < len(linea):
                    operandos = CalculadoraHija(acumulador, float(linea[y]))
                    try:
                        acumulador = operandos.div()
                    except ZeroDivisionError:
                        sys.exit("Error: Division by zero is not allowed")
                    y = y+1
                print(acumulador)
