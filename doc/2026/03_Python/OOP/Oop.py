

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


# 🔸Encapsulation :::::::::::::::::::::::::::::::

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

