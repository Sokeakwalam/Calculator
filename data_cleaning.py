import re

user_input = list(input('Please input a calculation you want: '))


def remove_empty_string():
    new_user_input = []
    for input in user_input:
        if input != " ":
            new_user_input.append(input)
    return new_user_input

def seperator():
    general_input = []
    inputs =  remove_empty_string()
    if inputs[0] == '-':
        inputs.insert(0, '0')
    b = ''
    for i, x in enumerate(inputs):
        if re.search("\d|\.", x):
           b += x
        if x == '+' or x == '-' or x == '*' or x == '/':
            general_input.append(b)
            general_input.append(x)
            b = ''
        if len(inputs)-1 == i:
            general_input.append(b)
    return general_input