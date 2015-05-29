#Objects and classes

# Classes let us define the blueprints for objects
from calendar import weekday


class Animal:
    # When defining a class's attributes, if they are preceded by __, it means they are private
    __name = ''
    __height = 0
    __weight = 0
    __sound = 0

    # Defining functions inside a class

    # Constructor with parameters
    def __init__(self, name, height, weight, sound):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound

    # Encapsulation with set and get functions:
    # Use the template 'props' in pyCharm to help writing them
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_height(self):
        return self.__height

    def set_height(self, height):
        self.__height = height

    def get_weight(self):
        return self.__weight

    def set_weight(self, weight):
        self.__weight = weight

    @property
    def get_sound(self):
        return self.__sound

    def set_sound(self, sound):
        self.__sound = sound

    # To use polymorphism, we will define a function, get_type, that will print the class name of the object
    def get_type(self):
        print("Animal")

    # to print all properties of an object we will create a toSting method:
    def toString(self):
        #as this method exists inside the class, it is not necessary to call the getters to obtain the information
        return "{} is {} cm tall and {} kilograms and says {}".format(self.__name, self.__height, self.__weight, self.__sound)


# Declaring and initializing an Object based on the class we just created
cat = Animal('Whiskers', 33, 10, 'Meow')

# Calling one of the methods from the Object
print(cat.toString())

# INHERITANCE

# To inherit from a class, we write the superclass in parentheses after the name of the subclass
class Dog(Animal):
    # once the inheritance is declared, the subclass gets all the variables and functions from the superclass
    __owner = ''

    #Overriding the constructor of the animal class
    def __init__(self, name, height, weight, sound, owner):
        self.__owner = owner
        # To determine that some of the objects variables will be handled by the superclass's constructor:
        super(Dog, self).__init__(name, height, weight, sound)

    # Writing getters and setters for variables that are not inherited:
    def get_owner(self):
        return self.__owner

    def set_owner(self, owner):
        self.__owner = owner

    # Defining the get_type function:
    def get_type(self):
        print("Dog")

    #Overriding the toString() function:
    #It is necessary to use the getter methods to invoke the superclass's properties.
    def toString(self):
        return "{} is {} cm tall and {} kilograms and says {}. His owner is {}".format(self.get_name(),
                                                                                       self.get_height(),
                                                                                       self.get_weight(),
                                                                                       self.get_sound,
                                                                                       self.__owner)

    #Method overloading
    def multiple_sounds(self, how_many=None):
        if how_many is None:
            print(self.get_sound)
        else:
            print(self.get_sound * how_many)

# Creating an object based on the subclass we just created

spot = Dog("spot", 53, 27, 'ruff', 'rurtubiac')

print(spot.toString())


#POLYMORPHISM

# allows us to refer to objects as their superclass and get their functions automatically
class AnimalTesting:
    def get_type(self, animal):
        animal.get_type()

test_animals = AnimalTesting()

test_animals.get_type(cat)
test_animals.get_type(spot)


spot.multiple_sounds(4)
print()
spot.multiple_sounds()