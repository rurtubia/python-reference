import random

#Basic for loop in python
for x in range(0, 10):
    # in this case we print every element in the same line
    print(x, '', end='')

print()
# looping through a list
grocery_list = ['juice', 'bananas', 'tomatoes']

for y in(grocery_list):
    print(y)

# defining a list of elements to cycle through
print()
for x in [2,6,8,10] :
    print(x)

# Doubling u for loops to cycle through a list

#We define a list of lists
num_list = [[1,2,3],[10,20,30],[100,200,300]]

print('Printing a list of lists:')
for x in range(0,3):
    for y in range (0,3):
        print(num_list[x][y])


#Basic while loop in python
#used when we don't know how many times we must loop

random_num = random.randrange(0,100)

while(random_num != 15):
    random_num = random.randrange(0,100)
    print(random_num)

#Traditional while loop

print('\nPrints pair numbers <= 9')
i = 0
while(i <= 20) :
    if(i%2 == 0) :
        print(i)
    elif(i == 9):
        break;
    else :
        i +=1
        continue
    i += 1