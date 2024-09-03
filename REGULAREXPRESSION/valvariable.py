#variable name
#1st char must be alphabet k to m
#2nd letter must be a number divisible by 3
#followed by any num of alphabets and numbers @

from re import fullmatch

variable=input("enter variable = ")

pattern="[k-m][369][a-zA-Z0-9@]*"

matcher=fullmatch(pattern,variable)

print("invalid "if matcher==None else "valid")
