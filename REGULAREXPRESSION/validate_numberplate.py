
f=open("C:\\Users\\Rintu Sam\\Desktop\\PythonJuneWorks\\REGULAREXPRESSION\\numberplate.txt","r")

write1=open("C:\\Users\\Rintu Sam\\Desktop\\PythonJuneWorks\\REGULAREXPRESSION\\vehiclenumberplate1.txt","w")

write2=open("C:\\Users\\Rintu Sam\\Desktop\\PythonJuneWorks\\REGULAREXPRESSION\\vehiclenumberplate2.txt","w")


pattern="(KL)[\d]{2}[A-Z]{1,2}[\d]{4}"



# for c in f:

#     if pattern==c:
#         write1.write(c)
    
#     else:
#         write2.write(c)

for year in f:
    y=year.rstrip("\n")

    if y==pattern:
        write1.write(str(y)+"\n")

    else:
        write2.write(str(y)+"\n")