class A:
    __count = 0        # set veriable as hidden
    def __init__(self):
        A.__count = A.__count+1
    def show(self):
        print("count = ",A.__count)


obj1 = A()


try:
    print(obj1.__count)      # generate an error due to __count is only accessile by class
finally:
    obj1.show()

