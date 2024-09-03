#power range
#2=>24[2+22]
#3=>369[3+33+333]

# num=int(input("enter number"))     2


# pattern=1

# for i in range(1,num+1):           1

#     pow=pow*10+num                 0*10+2   2*10+2    22*10+2

# print(pow)                         2       22     222......

num=int(input("enter number ")) 

sum=0

pattern=0

for i in range(1,num+1):

    pattern=pattern*10+num

    sum=sum+pattern

print(sum)