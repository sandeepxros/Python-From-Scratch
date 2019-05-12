class Add:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def Add(self):
        return self.x+self.y


add = Add(3, 4)
print("3+4 =", add.Add())

