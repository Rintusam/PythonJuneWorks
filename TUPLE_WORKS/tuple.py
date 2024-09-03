#TUPLE= (1,2,3,4)
#index positioning 
#duplicates allow
#immutable(cannot modify)
#insertion order preserved
#index()
#count()



numbers=[1,2,[3,(100,200,300),4],5,6]

num=numbers[2][1]

new_num=list(num)

new_num.append(500)

print(tuple(new_num))

numbers[2][1]=tuple(new_num)

print(numbers)