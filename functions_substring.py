# printing a substring:
long_string = 'this is a pretty long and boring string'
# to print the first three characters:
print(long_string[0:3])

# to print the last three characters:
print(long_string[-3:])

# to print everything except the last three characters:
print(long_string[:-3])

# concatenating substrings
print(long_string[:4] + ' is a war!')

# passing data to a string by datatype
print("%c is my first initial. "
      "My username is %s, "
      "my birth day is the %d "
      "and this is a random decimal number "
      "with five decimals: %.5f" %('r','rurtubia',28,0.76))

# capitalizing the first letter of a string
string2 = 'chile'
print(string2.capitalize())

# finding the index at which a substring can be found
print(long_string.find('pretty'))
# when the substring is not found, the result is -1
print(long_string.find('ugly'))

# finding if all the elements in a string are letters (not numbers)
print(string2.isalpha())
print(long_string.isalpha())

# finding out if all the elements in a string are numbers
print(string2.isalnum())

# finding out the length of a string
print(len(string2))

# replacing part of a string
print(long_string.replace('boring', 'meh'))
long_string = long_string.replace('this','    ')
print(long_string)

# stripping all white space from the beginning and end of a string
print(long_string.strip( ))
long_string = long_string.replace('    ','this')

# Splitting a string into a list
# the argument of the function determines how we want the words to be separated
long_string_list = long_string.split(' ')
print(long_string_list)