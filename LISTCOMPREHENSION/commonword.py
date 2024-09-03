words=["fly","float","flower","flat"]

#find common prefix

smallest_word=min(words,key=len)

print(smallest_word[::-1])

common_prefix=""

