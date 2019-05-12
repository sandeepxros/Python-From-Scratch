class Animal:
    pass
# pass is used for empty class otherwise it causes err

class Dog:
    pass


class GermanShepherd(Animal, Dog):
    pass


gs = GermanShepherd()
print(issubclass(GermanShepherd, Dog))  # issubclass returns t/f if the corresponding class is a subclass of another cls
print(issubclass(Dog, GermanShepherd))  # issubclass(subclassName , base class name)

print(isinstance(gs, GermanShepherd))  # isinsance(obj, class) return weather it is instance of that class or not
print(isinstance(gs, Animal))    # return true as inheririted class
