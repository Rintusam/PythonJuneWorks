#longest palidromic substring from given string

text="abbabbc"

# abab
# aba
# bb
# bab
# abba
longest_palindrome=""

for i in range(0,len(text)):

    left=i

    right=i

    while (left>=0 and right<len(text)and text[left]==text[right]):
    
        palindrome_text=text[left:right+1]

        if len(palindrome_text)>len(longest_palindrome):

            longest_palindrome=palindrome_text

        left=left-1

        right=right+1

print(longest_palindrome)


