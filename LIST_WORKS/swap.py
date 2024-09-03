num=[1,2,3,4,5,6,7]

# num[-1],num[0]=num[0],num[-1]

print(num.pop(0))

print(num.insert(0,num.pop()))
print(num.append(1))

print(num)
