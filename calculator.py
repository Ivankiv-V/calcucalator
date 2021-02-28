str_input = input("Delimoe: ")
delimoe = int(str_input)

operation = input ("+ / * - ^ ")
str_input2 = input("Delitel: ")
delitel = int(str_input2)

result = "Unknown"
if operation == "+":
	result = delimoe + delitel
elif operation == '/':
	result = delimoe / delitel
elif operation == "*":
	result = delimoe * delitel
elif operation == "-":
	result = delimoe - delitel
elif operation == "^":
	result = delimoe ** delitel
else:
	result = "Unknown"

print("Result: " + str(result))