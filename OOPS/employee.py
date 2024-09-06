

class person:

    def __init__(self,name,age,gender):

        self.name=name

        self.age=age

        self.gender=gender

    def display_person(self):

        print(self.name,self.age,self.gender)

class employee(person):

    def __init__(self,name,age,gender,eid,department,salary):

        super().__init__(name,age,gender)

        self.eid=eid

        self.department=department

        self.salary=salary

    def display_employee(self):

        super().display_person()

        print(self.eid,self.department,self.salary)

employee_instance=employee("rintu",22,"male","18","IT",150000)

employee_instance.display_employee()



