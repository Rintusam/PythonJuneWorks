#consonents= non vowels

text="aeiouqwrtyyy"

vowel="aeiou"

v_count=0

c_count=0

for ch in text:

    if vowel.count(ch)!=0:

        v_count+=1
    
    else:

        c_count+=1

print(f"vowels count = {v_count}")

print(f"consonent count = {c_count}")

