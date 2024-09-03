from re import finditer

text="abc123 @Kl#19Mdef"

# pattern="[abf]" #check either a b or f

# pattern="[a-k]"   #check for alphabets from a to k 

# pattern="[a-z]"  #check for all lowecase alphabets

# pattern="[A-Z]"  #check for all uppercase alphabets

# pattern="[a-zA-Z]"  #all alphabets

# pattern="[0-9]"  #check numbers

# pattern="[a-zA-Z0-9]"#all aphabets and digits

# pattern="[^a-zA-Z]" # excluding alphabets

# pattern="[^0-9]" # excluding gigits

# pattern="[^a-zA-Z0-9]" # excluding alphabets and digits

# pattern="[\s]"   #check for space

pattern="[^a-zA-Z0-9\s]" # excluding alphabets,digits,spaces



matcher=finditer(pattern,text)

for m in matcher:

    print(m.start(),"==",m.group())