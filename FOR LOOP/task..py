num=int(input("enter number"))

sum= 0
digit =0

for i in range(1,num+1):
    
    digit=digit*10+num

    sum=sum+digit

print(sum)
