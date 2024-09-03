text="ABCADD"

#print first recursive charcater
word_count={}

for w in text:

    if w in word_count:
        print(w,"first recurcive character")
        break

        
    else:

        word_count[w]=1
    

