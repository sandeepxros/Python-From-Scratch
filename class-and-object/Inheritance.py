class Teacher:
    name =''
    id = 0

    def show(self,name,id):
        self.name = name ;
        self.id = id ;
        print("id : ", self.id, " \nName: "+self.name)


st1 = Teacher()
st1.show('John', 1234556)


class Employee():            # derived class

    def emp(self):         # override method from base calss
        print("he is the Emp")


#st2 = Employee()
#st2.show("John",32141)

class IsAGoodMan(Teacher,Employee):  #multilavel inheritance

    def is_a_good_man(self):
        print("Is also a good Man")


st3 = IsAGoodMan()
st3.show("John", 12345)
st3.emp()
st3.is_a_good_man()