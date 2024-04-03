class Student:
    student_name="Ganesh"
    student_id=531

class Department:
    Dept_id="A"
    Dept_name="Computer Science"

class College(Student, Department):
    Clg_name="CMR Engineering College"
    Clg_Address="Medchal, Hyderabad"

Clg=College()
print(Clg.student_name)
print(Clg.Dept_name)
print(Clg.Clg_name)
