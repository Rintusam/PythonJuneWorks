#write a program to check number is palindrome or not

#121 is a palindrome number     (num=reversed num =palindrome)

#123 is not a palindromic number


num=int(input("enter number "))  #123

result=0

original=num

while(num!=0):  #123!=0     12!=0       1!=0   0!=0(false)

    digit=num%10  #123%10=3     12%10=2    

    num=num//10 #123//10=12     12//10=1  1//10=0
    
    result=result*10+digit  
    
print(result)

if(result==original):

    print(f"palindrome number")

else:
    print(f"not palindrome")


