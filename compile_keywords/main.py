'''
combine each word from variables.txt with each one from constants.txt
constants.txt has placeholder ($$$) for determining the position of where the variable will get placed
resulting combinations will get saved into compiled.txt
'''

PLACEHOLDER = '($$$)'
RESULTS_SEPARATOR = '\n\n'
variables = []
constants = ''

with open('variables.txt', 'r') as fv:
    for line in fv:
        variables += line.replace('\n', '').split(',')

with open('constants.txt', 'r') as fc:
    for line in fc:
        constants += line


with open('compiled.txt', 'w') as fr:
    text = ''
    for var in variables:
        text += constants.replace(PLACEHOLDER, var)
        text += RESULTS_SEPARATOR
    fr.write(text)