class Employee:
    a=23
    b=12
    c=3
    @classmethod       # This make the attributes like a, b, c are properties of a cls
    def setAtrrs(cls, a, b, c):
        cls.a=a
        cls.b=b
        cls.c=c
    @property             # It is getter works to get or access the values 
    def length(self):
        return self.a

    @length.setter
    def length(self, Value):
        self.a=Value

     

emp=Employee()
print(Employee.a)    # All these a,b,c are properties of a class and not the object
print(Employee.b)    #
print(Employee.c)
emp.setAtrrs(43, 56,3)
print(Employee.a)
# emp.length=5        # When we try to change the value of a without a setter method (AttributeError: property 'length' of 'Employee' object has no setter)
emp.length=9        # Now after writing the setter method its will change to 9
print(emp.length)   # If i use this with a property decorator python will throwns <bound method Employee.length of <__main__.Employee object at 0x0000015707671D10>>
# In order to acess this as a attribte we have to use Property decorator
# print(emp.length())  #This works as a method not like an attribute