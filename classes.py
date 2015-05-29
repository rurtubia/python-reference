#Objects and classes

# Classes let us define the blueprints for objects
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