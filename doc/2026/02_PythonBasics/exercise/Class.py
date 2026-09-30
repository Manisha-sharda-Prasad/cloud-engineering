# ⭐️:::::: Class  :::::::

# 🔸  ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
class Kettle(object):
    def __init__(self, make, price):
        self.make = make
        self.price = price

kirkland = Kettle("Kirkland", 8.99)
print(kirkland.price, kirkland.make)

hamilton = Kettle("Hamilton", 18.99)
hamilton.price = 12.00
print(hamilton.price, hamilton.make)

print("Models: {} = {}, {} = {}".format(kirkland.make, kirkland.price , hamilton.make, hamilton.price))