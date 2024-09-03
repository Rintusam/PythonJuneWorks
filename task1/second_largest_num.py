num1=int(input("enter number1 = "))

num2=int(input("enter number2 = "))

num3=int(input("enter number3 = "))

if num1>num2 and num1>num3:
    
    if num2>num3:
        print(f"the second largest number is {num2}")
    else:
        print(f"the second largest number is {num3}")


elif num2>num1 and num2>num3:
  
    if num1>num3:
        print(f"the second largest number is {num1}")
    else:
        print(f"the second largest number is {num3}")
        
          
elif num3>num1 and num3>num2:
    
    if num1>num2:
        print(f"the second largest number is {num1}")
    else:
        print(f"the second largest number is {num2}")