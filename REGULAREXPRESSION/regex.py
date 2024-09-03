from re import finditer

text="abababbab"

matcher=finditer("ab",text)  #(start,group)

count=0

for m in matcher:

    print(m.start(),"==",m.group())

    count+=1

print("no of ab = ",count)