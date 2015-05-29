# the statements if, else and elif are used to evaluate logical conditions
# the conditions refer to wether two things are equal to (==),not equal to (!=), greater than(>),
# greater than or equal to (>=), less than (<), less than or equal to (<=)

#The if statement executes code if a condition is met.

age = 23

if  age > 16 :
    print('You are old enough to drive')

else :
    print('You are not old enough to drive')

if age >=21 :
    print('you are old enough to drive a tractor trailer')
elif age >= 16 :
    print('You are old enough to drive a car')
else :
    print('You are not old enough to drive')


# The previous statements can be combined with logical operators: (and, or, not)

if((age >= 1) and (age <= 18)) :
    print('You get a birthday')

elif (age == 21) or (age >= 26) :
    print('You get a birthday')

elif not(age == 30) :
    print('You don\'t get a birthday')

else :
    print('You get a birthday party')


