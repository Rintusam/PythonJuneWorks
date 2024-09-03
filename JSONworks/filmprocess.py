from json import load

f=open("C:\\Users\\Rintu Sam\\Desktop\\Python_Works_2\\JSONworks\\films.json","r")

films=load(f)

for fl in films:

    print(fl.get("title"))