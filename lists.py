#   Allows creating a list of values and then manipulating them
#   Python is 0-based

#Declaring a list
grocery_list = ['Juice', 'Tomatoes', 'Potatoes', 'Bananas']

#Prints one element from the list
print('First Item:', grocery_list[0])

#Changing values of items in a list
grocery_list[0] = 'Milk'
print('\nFirst Item after \'Milk\' was added in the position of \'Juice\':', grocery_list[0])

#Print a subset of a list
#First item is included, last item is excluded
print('\nPrint of a subset of the list: ',grocery_list[1:3])

#A list can contain other list(s) as item(s)
other_events = ['Wash car', 'Pick up kids', 'Cash Check']
to_do_list = [other_events, grocery_list, 3]
#Print a list of lists:
print('\nList of lists: ',to_do_list)
#Print a specific item inside a list of lists
print('The third element of the second list is: ' + (to_do_list[1][2]))

#Add items to a list
grocery_list.append('onions')
print('\nGrocery list with onions appended at the end of it:',grocery_list)

print()
#Add items to a list at a specific location
grocery_list.insert(1, 'Pickles')
print('Grocery list with picles inserted at index 1',grocery_list)

#eliminate elements from a list
grocery_list.remove('Potatoes')
print('\nGrocery list with potatoes removed:',grocery_list)

#sorting a list
grocery_list.sort()
print('\nSorted grocery list:',grocery_list)

#sorting a list in reverse order
grocery_list.reverse()
print('\nGrocery list reversed:', grocery_list)

#deleting an item from a list
del grocery_list[4]
print('\nGrocery list with item at index 4 removed:',grocery_list)

#Combining lists together
to_do_list2 = grocery_list + other_events
print('\nNew list combining the elements of 2 previous lists: ', to_do_list2)

#Obtaining the length of a list
print(len(to_do_list2))
print('There are',len(to_do_list2),'items in to_do_list2')

#Obtaining the maximum element in a list
number_list = [3, 15, -65, -67.6, 98.1]
print(max(number_list))
print(min(number_list))
print('The highest value in number_list is', max(number_list), 'and the lowest value in the same list is ', min(number_list))

#When working with strings, min and max obtain the max and min alphabetical values
print('The max alphabetical item in other_events is',max(other_events), 'and the min alphabetical item is ', min(other_events) )