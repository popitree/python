class Kettle(object):
    # class attribute
    # like static fields
    power_source = "electricity"

    # Init is constructor
    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


# self is just parameter, its presence is important
# we can call it any other name
kenwood = Kettle("Kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)
print(kenwood.on)

kenwood.price = 12.75
print(kenwood.price)

hamilton = Kettle("Hamilton", 14.55)

print("Models: {} = {}; {} = {}".format(kenwood.make, kenwood.price,
                                        hamilton.make, hamilton.price))

print("Models: {0.make} = {0.price}; {1.make} = {1.price}"
      .format(kenwood, hamilton))

print(hamilton.on)
hamilton.switch_on()

print(hamilton.on)

# In python every type is also a class
# functions that is part of a class is called Method
# Main diffrence is Method has "self"

Kettle.switch_on(kenwood)
print("Kenwood Status:" + str(kenwood.on))

print("*" * 80)

# dynamic, but subclass might be preferable way to extend
kenwood.power = 1.5
print(kenwood.power)
# Error as Kettle does not have power and hamilton instance also
# print(hamilton.power)

print(Kettle.power_source)
print(kenwood.power_source)
kenwood.power_source = "fire"
# Now kenwood got its own data attribute that shadows class attribute
# Hence will be present in __dict__
# java wont allow to access/change static variable through instance
print(kenwood.power_source)
print("*" * 80)

# dict to get all attributes
print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)
