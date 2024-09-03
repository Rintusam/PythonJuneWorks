#date  01 1,10,11,12,19,31

from re import fullmatch

date=input("enter date = ")

pattern="(0?[1-9]|1[0-9]|2[0-9]|3[0-1])"

matcher=fullmatch(pattern,date)

print("invalid" if matcher==None else "valid")