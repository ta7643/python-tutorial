
# takes user input
x = int(input('Enter an integer: '))
y = int(input('Enter another integer: '))

# format pattern/template
formatStr = '{0} + {1} = {2}; {0} * {1} = {3}.'

print (formatStr.format(x, y, x+y, x*y))

# the same thing
equations = formatStr.format(x, y, x+y, x*y)
print(equations)
