from re import fullmatch

variable=input("enter passport id = ")

pattern="[A-z][1-9][\d][0\s][0-9]{4}[1-9]"

matcher=fullmatch(pattern,variable)

print("invalid" if matcher== None else "valid")

