words=["red","red","yellow","white","white","blue","white","white","yellow"]

# print word count


word_set=set(words)


for w in word_set:

    print(w,words.count(w))