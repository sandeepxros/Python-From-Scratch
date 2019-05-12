class Student:
    count = 0

    def __init__(self):
        Student.count += 1


student1 = Student()
student2 = Student()
student3 = Student()
student4 = Student()
student5 = Student()
student6 = Student()

print("total : ", Student().count, " Objects")


