


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