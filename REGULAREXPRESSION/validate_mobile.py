# validate mobile number with cpuntry code
#10 digits
#numbers starting with 6789

from re import fullmatch

phone_number=input("enter number = ")

pattern="(91)\s?[6-9][0-9]{9}"

matcher=fullmatch(pattern,phone_number)

print("invalid" if matcher== None else "valid")

