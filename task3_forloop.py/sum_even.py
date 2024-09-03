#pgm to print the sum of even numbers fron 1 to 100


sum=0
for i in range(1,101):

    if i%2==0:

        sum=sum+i
        
print(sum)