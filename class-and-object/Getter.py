class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id


student_obj = Student("John", 21343221)

print(getattr(student_obj, 'name'))  # getattr(obj_name, attribute) used for getting value of class variables
setattr(student_obj, 'name',"Shan")  # setattr(obj_name , attribute  , value) used for set value of class veriables
print(student_obj.name)
delattr(student_obj,'name')  # used for deleting an attribute
# print(student_obj.name) # will generate an error because we have deleted the attribute
print(hasattr(student_obj, 'name')) # return if the class have given attribute or not
print(student_obj.__doc__)    # It contains a string which has the class documentation
print(student_obj.__dict__)   #  It provides the dictionary containing the information about the class namespace
print(student_obj.__module__)  # It is used to access the module in which, this class is defined.


