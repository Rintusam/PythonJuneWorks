# validate pancard number

# first 3 character are alphabets

# 4 th place PCAFHT

# 5th place alphabet

# 4 digit
 
# 1 alphabet

from re import fullmatch

variable=input("enter variable = ")

pattern="[A-Z]{3}[PCAFHT][A-Z][\d]{4}[A-Z]"

matcher=fullmatch(pattern,variable)

print("inavlid" if matcher==None else "valid")