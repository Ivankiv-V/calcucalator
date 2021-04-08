import math
stroka = []
def spis(x, y):
    for i in range(max(len(x), len(y))):
        if i < len(x):
            stroka.append(x[i])
        if i < len(y):
            stroka.append(y[i])
    return stroka

def parse_command(command: str) -> list:
    parsedlone = command.replace(' ', '')
    res = list(parsedlone)
    return res

def calc(command: str) -> float:
    hp_ops = tuple('^')
    mp_ops = ('*', '/')
    lp_ops = tuple('+-')
    supported_ops = hp_ops + mp_ops + lp_ops
    digit_chars = tuple('0123456789.-')

    actions = list()
    d = dict()
    d['opr'] = 'First'
    d['val'] = ''
    actions.append(d)
    instr = ''.join(parse_command(command))
    for i, letter in enumerate(instr):
        if letter in supported_ops and (i > 0) and actions[-1]['val'] != '':
            actions.append({'opr': letter, 'val': ''})

        elif letter in digit_chars:
            actions[-1]['val'] += letter

    i = 0
    actions.reverse()

    while i < len(actions):
        action = actions[i]
        operation = action.get('opr')
        if operation in hp_ops:
            if operation == '^':
                pre_res = float(actions[i + 1].get('val')) ** float(action.get('val'))
                actions[i + 1]['val'] = str(pre_res)
                del actions[i]
        else:
            i += 1
    actions.reverse()

    i = 0
    result = '0'
    error = False
    while i < len(actions):
        action = actions[i]
        operation = action.get('opr')
        if operation in mp_ops:
            if float(action.get('val')) == 0 and operation == '/':
                result = 'inf'
                error = True
            else:
                eval_str = (actions[i - 1].get('val') + operation + action.get('val'))
                pre_res = eval(eval_str)
                actions[i - 1]['val'] = str(pre_res)
            actions.pop(i)
        else:
            i += 1

    if not error:
        for action in actions:
            chislo_A = result
            chislo_B = action.get('val')
            operation = action.get('opr')
            if operation in lp_ops:
                result = str(eval(chislo_A + operation + chislo_B))
            else:
                result = chislo_B
    return result

def getfromfile(file_name: str):
    with open(file_name, 'r') as f:
            line = f.readlines()
    return line

i = 0
import sys
if len(sys.argv) <= 1:
    command = input("Что вычислить? ")
    print(calc(command))
else:
    filename = sys.argv[1]
    f = open('output.txt', 'w')
    f.close()
    command = getfromfile(filename)
    c = len(command)
    for i in range(c):
        y = calc(command[i])
        print(y)
        with open('output.txt', 'a') as f:
            f.writelines(str(y) + '\n')
