

entered_number = int(input("Please enter a number: "))

if (entered_number % 3 == 0) and (entered_number % 5 == 0):
	print("Fizz Buzz") 
elif (entered_number % 3 == 0) and (entered_number % 5 != 0):
	print("Fizz")
elif (entered_number % 5 == 0) and (entered_number % 3 != 0):
	print("Buzz")