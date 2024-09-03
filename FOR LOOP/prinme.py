#prime number or not

num=int(input("enter number = "))

isPrime=True

for i in range(2,num):

    if num%i==0:

        isPrime=False

        break
    
print(f"is prime" if isPrime==True else f"not prime")