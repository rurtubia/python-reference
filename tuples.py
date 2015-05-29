#   The main difference between a tuple and a list is that the contents of a tuple cannot be changed afterwards

# declaring a tuple
pi_tuple = (3,1,4,1,5,9)
print('The new tuple is: ', pi_tuple)
#converting a tuple into a list:
new_tuple = list(pi_tuple)

#converting a list into a tuple:
new_list = tuple(new_tuple)

#obtaining the length of a tuple
len(new_tuple)
print('The length of the tuple is', len(new_tuple))

#obtaining the minimum value in a tuple
min(new_tuple)
print('The minimum value in the tuple is', min(new_tuple))

#obtaining the maximum value in a tuple
max(new_tuple)
print('The maximum value in the tuple is', max(new_tuple))
