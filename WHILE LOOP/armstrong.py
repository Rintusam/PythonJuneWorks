

num=(int(input("enter number = ")))

original=num

total=0

digit_count=len(str(num))

while(num!=0):

    digit=num%10

    num=num//10

    exponent=digit**digit_count

    total=total+exponent
print(total)
print("amstrong number"if original==total else "not Armstrong")


   