class Employee:
    a=23
    b=12
    c=3
    @classmethod       # This make the attributes like a, b, c are properties of a cls
    def setAtrrs(cls, a, b, c):
        cls.a=a
        cls.b=b
        cls.c=c

emp=Employee()
print(Employee.a)    # All these a,b,c are properties of a class and not the object
print(Employee.b)    #
print(Employee.c)
emp.setAtrrs(43, 56,3)
print(Employee.a)
print(Employee.b)
print(Employee.c)
