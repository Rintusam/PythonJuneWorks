num1=int(input("enter number1 = "))

num2=int(input("enter number2 = "))

num3=int(input("enter number3 = "))

if num1<num2<num3:
    print(f"the numbers in sorted (ascending) order is {num1},{num2},{num3}")

elif num2<num3<num1:
    print(f"the numbers in sorted (ascending) order is {num2},{num3},{num1}")
          
elif num3<num1<num2:
    print(f"the numbers in sorted (ascending) order is {num3},{num1},{num2}")

    