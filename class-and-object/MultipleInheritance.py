class Animal:
    def animal(self):
        print("All animals are the subset of this class")

class Dog:
    def dog(self):
        print("Dog is the subset of animal")

class puppy:
    def puppy(self):
        print("puppy is the subset of dog class")

class GermanShepherd(Animal,Dog,puppy):   # Multiple inheritance have more than one base class
    def gs(self):
        print("german shepherd is a Animal, a dog and may be a puppy")


gs = GermanShepherd();
gs.animal()
gs.dog()
gs.puppy()
gs.gs()
