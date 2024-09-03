#read a number and extract digits from number

#sample input=123
#output:
    #3
    #2
    #1

number=int(input("enter number = "))

while(number!=0):

    digit=number%10

    number=number//10

    print(digit)