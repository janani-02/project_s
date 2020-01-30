class person(object):
    def _init_(self,name,idnumber):
        self.name=name
        self.idnumber=idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)


class Employee(person):
    def _init_(self,name,idnumber,salary,post):
        self.salary=salary
        self.post=post
        person._init_(self,name,idnumber)
a=person('rahul',88602)
print(a)

class A:
    def _init_(self,n='rahul'):
        self.name=n
class B(A):
    def _init_(self,roll):
        self.roll=roll
object=B(23)
print(pbject.name)
