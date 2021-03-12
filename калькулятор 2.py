str_command = input("введи команду")
sF =''
sS =''
str_A =''
str_B =''
operation =''
for letter in str_command:
    print(letter)
    if letter =='+' or letter =='-' or letter =='/' or letter =='*' or letter =='^':
        if str_A == '':
            sF = letter
        elif operation != '':
            sS = letter
        else:
            operation = letter
    else:
        if operation =='':
            str_A = str_A + letter
        else:
            str_B = str_B + letter
            
str_A = sFstr_A.strip()
str_B = str_B.strip()
print(str_A)
print(str_B)

c = float(str_A)
#print(type(c))

d = float(str_B)
#print(type(d))

if operation == '/':
    if B == 0:
        result = 'inf'
    else:    
        result = c / d
elif operation == '+':
    result = c + d
elif operation == '-':
    result = c - d
elif operation == '*':
    result = c * d
elif operation == '^':
    result = c ** d
else:
    result = "unknown"
#print(type(result))
print("Result: " + str(result))

