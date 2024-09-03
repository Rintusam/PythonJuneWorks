#read a number and print the sum of the digit

#input=456

#output=4+5+6

num=int(input("enter number"))

sum=0

while(num!=0):

    digit=num%10
    
    num=num//10

    sum=sum+digit

print(sum)

 