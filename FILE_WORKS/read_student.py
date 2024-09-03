f=open("C:\\Users\\Rintu Sam\\Desktop\\PythonJuneWorks\\FILE_WORKS\\students.txt","r")

students=[]

for stud in f:

    students.append(stud.rstrip("\n"))

print(students)

   