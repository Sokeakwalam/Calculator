import re

def clean_data(user_input):
# remove empty strings
    clean_user_input = []
    for inputs in user_input:
        if inputs != " ":
            clean_user_input.append(inputs)

# Group/seperate input based on operators and numbers including decimal
    general_input = []
    if clean_user_input[0] == '-':
        clean_user_input.insert(0, '0')
    b = ''
    for i, x in enumerate(clean_user_input):
        if re.search("\d|\.", x):
           b += x
        if x == '+' or x == '-' or x == '*' or x == '/':
            general_input.append(b)
            general_input.append(x)
            b = ''
        if len(clean_user_input)-1 == i:
            general_input.append(b)
    return general_input