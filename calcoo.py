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


if __name__ == "__main__":
    try:
        variable = Calculadora(float(sys.argv[1]), float(sys.argv[3]))
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    if sys.argv[2] == "suma":
        print(variable.suma())
    elif sys.argv[2] == "resta":
        print(variable.resta())
    else:
        sys.exit("Solo se admite suma o resta")
