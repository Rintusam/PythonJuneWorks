#create a function is_palindrome(word) return True if word is palindromic string
#else return false


def is_palindrome(word):

    reverse_str=word[::-1]

    return word==reverse_str

print(is_palindrome("malayalam"))