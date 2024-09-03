email_ids=[
         "rintu@gmail.com",
         "rosh@gmail.com",
         "parv@gmail.com",
         "shebu@gmail.com",
         "suhaib@gmail.com"
]

f=open("C:\\Users\\Rintu Sam\\Desktop\\PythonJuneWorks\\FILE_WORKS\\email_id.txt","w")

for email in email_ids:
    f.write(email+"\n")