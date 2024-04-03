# MultiLevel Inheritance 

class GrandFather:          # 1st Parent class 
    Grdf_name="Jhon"
    Properties="100cr"

class Father(GrandFather):  # 2nd child class which consists of properties of their own and thier father
    F_name="Michal"
    F_properties="150cr"

class Son(Father):         #  3rd Son class which contains the properties of theie grand father and father
    name="Michal Jhon"
    My_properties="250cr"

Myobj=Son()
print(Myobj.Grdf_name)
print(Myobj.Properties)
print(Myobj.My_properties)
print(Myobj.F_properties)
print(Myobj.name)

