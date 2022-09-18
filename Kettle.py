class Kettle(object):

    power_source = "electricity"
    def __init__(self,make,price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True

kenwood = Kettle("Kenwood",200)
hamilton = Kettle("Hamilton",399)
print(kenwood.price,"\n"+kenwood.make)

print("Models : \n{0.make} = {0.price},{1.make} = {1.price}".format(kenwood,hamilton))

"""
self is a refrence to instance of a class
___init__ is a constructor

"""

hamilton.switch_on()
print(hamilton.on)
Kettle.switch_on(kenwood)
print(kenwood.on)
print('*'*80)

kenwood.power = 1.5
print(kenwood.power)
print('*'*80)
print(Kettle.power_source)
print(kenwood.power_source)
print(hamilton.power_source)

print(kenwood.__dict__)
