class A:
    def add(self, a, b):
        return a+b


class B(A):
    def add(self, a, b, c):     # this is override 2nd line method
        return a+b+c


add = B()
print(add.add(3, 2, 4))