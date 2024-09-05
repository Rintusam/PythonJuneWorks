# creatinng calss

class Student:

    name:str

    id:int

    gender:str

    age:int

    contact=str

    department:str

    def __init__(self,id,name,age,gender,contact,department):

        self.id=id

        self.name=name

        self.age=age

        self.gender=gender

        self.contact=contact

        self.department=department

    

    def display_student(self):
        print(self.id,self.name,self.age,self.gender,self.contact,self.department)


# creating object 

student_instance=Student(100,"hari",22,"male",234567777,"Django")

student_instance.display_student()
