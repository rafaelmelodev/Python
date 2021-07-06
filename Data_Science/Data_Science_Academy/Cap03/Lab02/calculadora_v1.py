# Python Calculator

import math
import sys

# Print the menu to the user
print("******************PYTHON CALCULATOR*********************\n")
print("Selecione o número da operação desejada:\n")
print("1 - Soma \n2 - Subtração \n3 - Multiplicação \n4 - Divisão")

# Request the desired menu option and the number to be operated
operation = input("\nDigite a opção desejada (1/2/3/4):")
firstNumber = float(input("\nDigite o primeiro número:"))
secondNumber = float(input("Digite o segundo número:"))

if operation == '1':
    result = firstNumber + secondNumber
    signal = '+'
elif operation == '2':
    result = firstNumber - secondNumber
    signal = '-'
elif operation == '3':
    result = firstNumber * secondNumber
    signal = '*'
elif operation == 4:
    result = firstNumber / secondNumber
    signal = '/'
else:
    print("Operação inválida!\n")
    sys.exit()
    
# Show the solution to the user
print("O resultado da operação", firstNumber, signal, secondNumber,"=", result)

#End of calculator