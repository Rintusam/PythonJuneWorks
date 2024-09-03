#numbers=[1,2,[3,(100,200,300),4],5,6]   =>    [1,2,[3,4,(100,150,200,300)5,6]

numbers=[1,2,[3,(100,200,300),4],5,6]

new=numbers[2]

ele_four=new.pop()

new.insert(1,ele_four)

new1=numbers[2][2]

list1=list(new1)

list1.insert(1,150)

tuple1=tuple(list1)

numbers[2][2]=tuple1

print(numbers)



