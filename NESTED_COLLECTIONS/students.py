students=[

{"id":100,"name":"rintu","course":"fullstack","mark":500},
{"id":100,"name":"roshu","course":"fullstack","mark":480},
{"id":100,"name":"paru","course":"mernstack","mark":490},
{"id":100,"name":"arjun","course":"testing","mark":460},
{"id":100,"name":"shebu","course":"asp","mark":400},
{"id":100,"name":"ahamed","course":"aspk","mark":430},
{"id":100,"name":"suhaib","course":"mernstack","mark":450},
]

#print all student names

# for st in students:
#     print(st.get("name"))

# student_name=[st.get("name") for st in students]
# print(student_name)

# all_courses=[st.get("course") for st in students]
# print(all_courses)

# fullstack_stud=[st.get("name") for st in students if st.get("course")=="fullstack"]
# print(fullstack_stud)

# #print students name whose mark is  from 450-480

# mark_range=[st.get("name")for st in students if st.get("mark") in range(450,481)]
# print(mark_range)

# max_mark=0
# for st in students:
#     if st.get("mark")>max_mark:
#         max_mark=st.get("mark")
# highest_mark=[st.get("name")for st in students if st.get("mark")==max_mark]
# print(highest_mark)

def get_mark(stud):
    return stud.get("mark")
top_student=max(students,key=get_mark)
print(top_student)

max_mark_stud=max(students,key=lambda st:st.get("mark"))
print(max_mark_stud)

sorted_students=sorted(students,key=get_mark)
print(sorted_students)

total=sum([st.get("mark")for st in students])
print(total)