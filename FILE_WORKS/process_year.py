f_read=open("C:\\Users\\Rintu Sam\\Desktop\\Python_Works_2\\FILE_WORKS\\years.txt","r")
f_century=open("C:\\Users\\Rintu Sam\\Desktop\\Python_Works_2\\FILE_WORKS\\century_year.txt","w")
f_non_century=open("C:\\Users\\Rintu Sam\\Desktop\\Python_Works_2\\FILE_WORKS\\non_century_year.txt","w")


for year in f_read:
    y=int(year.rstrip("\n"))

    if y%100==0:
        f_century.write(str(y)+"\n")

    else:
        f_non_century.write(str(y)+"\n")