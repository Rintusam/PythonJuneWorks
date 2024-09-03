word1="PQRST"

word2="ABC"

smallest_word= word1 if len(word1)<len(word2) else word2

merged_string=""

for i in range(0,len(smallest_word)):

    merged_string=merged_string+word1[i]+word2[i]

if len(word1)>len(word2):

    balance_word=word1[len(smallest_word):]

else:
    balance_word=word2[len(smallest_word):]

merged_string=merged_string+balance_word

print(merged_string)
                        
