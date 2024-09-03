f=open("C:\\Users\\Rintu Sam\\Desktop\\Python_Works_2\\FILE_WORKS\\Land_slide.txt","r")

data=[]

for line in f:

    lst=line.rstrip("\n").split(" ")

    dic={"state":lst[0], "year":lst[1], "death_count":int(lst[2])}
    
    data.append(dic)


state_summary={}

for dic in data:
    state=dic.get("state")
    death_count=dic.get("death_count")

    if state in state_summary:
        state_summary[state]+=death_count

    else:
        state_summary[state]=death_count
print(state_summary)
