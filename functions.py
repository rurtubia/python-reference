#sys is imported to get input:
import sys

# A function's definition starts with the keyword def
# after that, parameters can be added inside the parenthesis
# those parameters can be used and returned as defined in the function body

def addNumber(firstNumber, lastNumber):
    sumNumbers = firstNumber + lastNumber
    return sumNumbers


print(addNumber(1, 5))

# due to code scope limitations, it is impossible to use what is declared inside a function body outside of it:
# e.g:          print(sumNumbers)
# would return:  NameError: name 'sumNumbers' is not defined

#Getting input from the user:
print('What is your name?')
name = sys.stdin.readline()

print('Hello, ',name)


