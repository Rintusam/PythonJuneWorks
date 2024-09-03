def is_kangaroo_word(word,lookup_word):

    return len(word)>len(lookup_word)

word="watermelon"

lookup_word="melons"

print(is_kangaroo_word(word,lookup_word))