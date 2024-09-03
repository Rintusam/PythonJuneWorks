number=int(input("enter number = "))

prime_number=True

for i in range(2,number):

    if(number%i==0):

        prime_number=False

        break
        
        
if prime_number==True:
    print(f"prime number")
else:
    print(f"not a prime")

