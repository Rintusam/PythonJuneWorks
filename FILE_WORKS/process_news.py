f=open("C:\\Users\\Rintu Sam\\Desktop\\Python_Works_2\\FILE_WORKS\\news.txt","r")
word_list=[]

# for line in f:
#     words=line.rstrip("\n").split(" ")
   
    
#     for w in words:

#         word_list.append(w)

# print(word_list)

word_list=[w for line in f for w in line.rstrip("\n").split(" ")]


word_count={w:word_list.count(w)for w in word_list}
print(word_count)

srt=sorted(word_count,key=lambda key:word_count.get(key),reverse=True)
print(srt)

