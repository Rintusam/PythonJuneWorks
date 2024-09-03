# num=[2,5,7,3,1,6,8]

# num.sort()

# print(num[0])



num=[2,5,7,3,1,6,8]

smallest_num=num[0]

for i in num:

    if i < smallest_num:

        smallest_num=i

print(f"smallest number is {smallest_num}")

