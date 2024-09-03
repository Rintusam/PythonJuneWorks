number=[0,2,6,8]

missing_even_num=[]

max_number=max(number)#8

for num in range(0,max_number+1,2):
    if num not in number:
        missing_even_num.append(num)
print(missing_even_num)

