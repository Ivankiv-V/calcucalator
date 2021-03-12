str_input = input("Delimoe: ")
delimoe = int(str_input)

operation = input ("+ / * - ^ ")
str_input2 = input("Delitel: ")
delitel = int(str_input2)

if operation == "+":
	result = delimoe + delitel
elif operation == "/":
         if delitel != 0:
                 result = delimoe / delitel
         else:
               result = "Inf"         
 
elif operation == "*":
        result = delimoe * delitel
elif operation == "-":
	 result = delimoe - delitel
elif operation == "^":
        result = delimoe ^ delitel

	
print("Result: " + str(result))

