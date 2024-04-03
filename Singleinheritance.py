# A basic single inheritance which contains base and derived class

class Employee:    # Creating a base class
    name="Donglee"

class Programmer(Employee):   # Creating a desired class
    salary=30000

pr=Programmer()    # Creating an object for Derived class which will get all the properties of base class
print(pr.name)
print(pr.salary)

em=Employee()
print(em.salary)  #'Employee' object has no attribute 'salary'
