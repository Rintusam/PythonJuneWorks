num=[10,10,20,20,20,21,22,23]
  
num_set=set(num)

orginal= num.copy()
unique=[]
for i in num_set:

   print(i,num.count(i))


#non repeat
for j in orginal:
    if orginal.count(j)==1:
        unique.append(j)
print(unique)
