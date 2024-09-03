# starting with alphanumeric
# [a-zA-Z0-9._]
# @gmail.com

from re import fullmatch

variable=input("enter gmail = ")

pattern="[\w][\w._]*(@gmail.com)"

matcher=fullmatch(pattern,variable)

print("invalid" if matcher==None else " valid")