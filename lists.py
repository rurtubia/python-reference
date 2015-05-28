#   Allows creating a list of values and then manipulating them
#   Python is 0-based

#Declaring a list
grocery_list = ['Juice', 'Tomatoes', 'Potatoes', 'Bananas']

#Prints one element from the list
print('First Item:', grocery_list[0])

#Changing values of items in a list
grocery_list[0] = 'Milk'
print('First Item:', grocery_list[0])

#Print a subset of a list
#First item is included, last item is excluded
print(grocery_list[1:3])

#A list can contain other list(s) as item(s)
other_events = ['Wash car', 'Pick up kids', 'Cash Check']

to_do_list = [other_events, grocery_list, 3]

#Print a list of lists:
print(to_do_list)
print()
#Print a specific item inside a list of lists
print('the third element of the second list is: ' + (to_do_list[1][2]))