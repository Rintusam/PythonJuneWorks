number=int(input("enter the number = "))
sum=0 

while(number!=0 ):
    if number==1:
        number=0

    digit=number%10
    number=number//10
    
    sum=sum+digit 

print(sum)
