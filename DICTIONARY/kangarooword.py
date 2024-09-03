source_word="CHICKEN"

target_word="HEN"

word_count={}

for ch in source_word:

    if ch in word_count:
        
        word_count[ch]+=1

    else:

        word_count[ch]=1

# print(word_count){'C': 2, 'H': 1, 'I': 1, 'K': 1, 'E': 1, 'N': 1}
is_kangaroo_word=True

for ch in target_word:

    if ch in word_count and word_count.get(ch)>0:

        word_count[ch]-=1
    else:
        is_kangaroo_word=False

print(is_kangaroo_word)




