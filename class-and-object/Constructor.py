class Students:
    def __init__(self, name, id): # __init__ method is used for declaring constructor in python
        self.id = id
        self.name = name

    def display(self):
        print("Student name "+self.id+"\nStudent name : "+self.name)


student1 = Students("Ram", "1232321")
student1.display()
student2 = Students("Ram", "1232321")
student2.display()

