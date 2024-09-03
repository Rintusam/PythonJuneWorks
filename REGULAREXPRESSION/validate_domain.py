from re import fullmatch

f=open("C:\\Users\\Rintu Sam\\Desktop\\PythonJuneWorks\\REGULAREXPRESSION\\domain.txt","r")

pattern=".*.com"

for line in f:

    domain=line.rstrip("\n")
    
    matcher=fullmatch(pattern,domain)

    if matcher !=None:

        print(domain)


