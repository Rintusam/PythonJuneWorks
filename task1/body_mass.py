weight=int(input("enter weight = "))

height=int(input("enter height = "))

height_in_meter=height/100

bmi=weight/height_in_meter**2

print(f"bmi = {bmi}")

if bmi<19:
    print(f"The Person is UNDER WEIGHT ")

elif bmi<=19:
    print(f"The person is heaving NORMAL WEIGHT ")
elif bmi<=25:
    print(f"The person is heaving NORMAL WEIGHT ")

elif bmi<=25:
    print(f"The Person is OVER WEIGHT ")
elif bmi<=30:
    print(f"The Person is OVER WEIGHT ")

else:
    print(f"OBESITY")


    
