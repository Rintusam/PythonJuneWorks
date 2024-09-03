from re import finditer

text="ab12xyz678pqr123cdef"

# pattern="[a-z]{3}" ,#matching continious 3 aplhabets 

# pattern="[0-9]{3}",#matching continuos 3 digits

# pattern="([c-h]|[t-z])"

pattern="([a-zA-Z]{3}|[0-9]{3})"

matcher=finditer(pattern,text)

for m in matcher:

    print(m.start(),"==",m.group())