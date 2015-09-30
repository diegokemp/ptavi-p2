#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

class Calculadora():

    def __init__(self, operando1, operacion, operando2):
        self.operando1 = operando1
        self.operacion = operacion
        self.operando2 = operando2

    def suma(self):
        return self.operando1 + self.operando2
    

if __name__ == "__main__":

        variable = Calculadora(float(sys.argv[1]), sys.argv[2], float(sys.argv[3]))
        print(variable.suma())
