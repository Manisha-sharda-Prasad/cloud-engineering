

# 🔸Class & Objects :::::::::::::::::::::::::::::::
# Objects are the instances of the Class, Objects has Properties, Name, Methods

class User:
    def __init__(self):                  #Constructor, starts with __init___, must have at-least 1 parameter(self).
        self.name = 'sampleName'         #attributes: var inside a class, Also properties.
        self.age = 'sampleAge'

    def intro(self):                     #self parameter: refers to the current object
        print("Hello I am ",self.name)
        print("I am ",self.age, "years old.")

sampleUser = User()
sampleUser.intro()

print(sampleUser.name, sampleUser.age)


class SampleUser:
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def intro(self):
        print("Hello I am ",self.name)
        print("I am ",self.age, "years old.")

sampleUser = SampleUser("Anaya Pan", 23)
sampleUser.intro()

print(sampleUser.name, sampleUser.age)


# 🔸Encapsulation & Abstraction:::::::::::::::::::::::::::::::

class Car():
    def __init__(self, make, model, initial_speed = 0):
        self.make = make
        self.model = model
        if initial_speed < 0:
            self.speed = 0
        else:
            self.speed = initial_speed

    def speed_up(self):
        self.speed += 5
        print("After speeding up my car speed is ", self.speed)

    def speed_down(self):
        if self.speed < 5:
            self.speed = 0
        else:
            self.speed -= 5
            print("After slowing down my car speed is now ", self.speed)

    def current_speed(self):
        print("My current car speed is ",self.speed)


my_car = Car("Ford", "Mustang", 50)

#Calling all the methods inside class:
my_car.current_speed()
my_car.speed_up()
my_car.speed_down()


# 🔸Instance Variables::::::::::::::::::::::::::::::::
#Instance/Object Var : property on one obj dont interfere with another property of obj

class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

my_dog = Dog("Tedd", 2)
print(my_dog.__dict__)            #{'name': 'Tedd', 'age': 2}

my_dog.color = "brown"            #Added new property, was not defined in constructor
print(my_dog.__dict__)            #{'name': 'Tedd', 'age': 2, 'color': 'brown'}

del my_dog.age                    #deleting instance var
print(my_dog.__dict__)            #{'name': 'Tedd', 'color': 'brown'}


#Private __Property:::::::::::
class Cat():
    def __init__(self, name, age):
        # Double __Underscore makes it Private
        self.__name = name
        self.__age = age

my_cat = Cat("Roo", 4)
print(my_cat.__dict__)             #{'_Cat__name': 'Roo', '_Cat__age': 4}

#print(my_cat.__name, my_cat.__age) Error: 'Cat' object has no attribute '__name','__age'

