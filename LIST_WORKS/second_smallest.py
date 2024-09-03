num=[3,5,7,1,9,2,10,4]

smallest_num=num[0]

second_smallest_num=num[-1]

for i in num:

    if i < second_smallest_num and i < smallest_num:

        second_smallest_num=smallest_num
        
        smallest_num=i

    elif i < second_smallest_num and i > smallest_num:

        second_smallest_num=i

print(second_smallest_num)