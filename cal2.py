str_command = input("Please type your command a + b or a - b: ")

sign_A = '' 
sign_B = ''

str_A = ''
str_B = ''

operation = '' 
i = 0

while i < len(str_command) :
    if str_command[i] == '+' or str_command[i] == '-' or str_command[i] == '*' or str_command[i] == '/' or str_command[i] == '^' :
        if str_A == '': 
            sign_A = str_command[i]
        elif operation != '':
            sign_B = str_command[i]
        else:
            operation = str_command[i]
    else:
        if operation == '':
            str_A += str_command[i]
        else:
            str_B += str_command[i]
    i += 1

chislo_A=float(sign_A + str_A)
chislo_B=float(sign_B + str_B)

result = None

if operation=='/' :
    if chislo_B == 0:
        result = "Inf"
    else:
        result = chislo_A/chislo_B
elif operation=='*' : 
    result=chislo_A*chislo_B
elif operation=='-' : 
    result=chislo_A-chislo_B
elif operation=='+' : 
    result=chislo_A+chislo_B
elif operation=='^' : 
    result=chislo_A**chislo_B
else : 
    result='Введите оператор'

print("Result: " + str(result))
