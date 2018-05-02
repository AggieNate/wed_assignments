

first_number = int(input("Enter your first number: "))
second_number = int(input("Enter your second number: "))
operand = input("Enter an operand: ")

import Calculator

if operand == "+":
	result = Calculator.add(first_number, second_number)
	print(result)
elif operand == "-":
	result = Calculator.subtract(first_number, second_number)
	print(result)
elif operand == "*":
	result = Calculator.multiply(first_number, second_number)
	print(result)
elif operand == "/":
	result = Calculator.divide(first_number, second_number)
	print(result)
