#syntax for class
class Students:
    id = 12345 #calss variable
    name = "John"

    def student(self):
        print(self.id, self.name)
 #the self is used as a reference variable which refers to the current class object.
 # It is always the first argument in the function definition. However, using self is optional in the function call.

 #Synatax for creating instance
 #<object-name> = <class-name>(<arguments>)


student = Students()  #instance of the calss Students
student.student()    #dot operator used for access variables and methods of class
