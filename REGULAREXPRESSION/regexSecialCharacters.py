from re import finditer

text= "abc TN7klefg@3#$dbm"

pattern="[\w]"     #\d= print digits            \D print excuding digits
                   #\w print a-zA-Z0-9          \W print all specialcharcters and space
                   #\s print space              \Sexclude spce and print all

matcher =finditer(pattern,text)

for m in matcher:

    print(m.start(),m.group())

    # +  one or More 
    # *  zero or more
    # ?  optional