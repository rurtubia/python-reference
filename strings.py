"""
Multi line comment:
variables in python must start with a letter,
then it can have numbers or undersocres
"""

#   string variables can use either a single or double quotes
name = 'Randy'

#   to include quotes in a string, it is necessary to use a backslash
username = "\"rurtubia\""

#   to concatenate strings in python, a + sing is used
print('My name is '+ name + ' and my username name is ' + username)
# another way to concatenate strings in pythonn is this:
print("%s %s" %('my github username is ', username))

#to print more than one new line at the same time:
print("\n" * 3)

#to print two or more print() commands in a single line:
print("The first line has joined ", end="")
print("the second line.")


#   multi line quotes in python

multi_line_quote =  '''1) first line
2) second line
3) third line
'''

print(multi_line_quote)
# There are five main data types in python: numbers, strings, lists, tuples and dictionaries


