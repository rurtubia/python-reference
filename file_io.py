# we need to import the os module to be able to delete a file
import os
# Creating and opening a file

# to read and append to file, we use the command 'ab+' -it also opens and creates a file
# to write to this file, we use the command 'wb'

test_file = open('test.txt', 'wb')

# Finding out which file mode is in use
print(test_file.mode)

# Finding out the name of the file
print(test_file.name)

# Writing text to a file
test_file.write(bytes("Text to be written in the file\n", 'UTF-8'))

# Closing a file
test_file.close()

# Reading text from a file
test_file = open('test.txt', 'r+')

# Obtaining the text from a .txt file
text_in_file = test_file.read()

# Printing the text from a file to the screen
print(text_in_file)


# Deleting a file
# it throws an error if the file hasn't been closed beforehand
test_file.close()
os.remove('test.txt')
