#anagram                      source word== target word(equal num of letters and same letters with diff position)
                                            

# source_word="listen"

# target_word="silent"

# srt_source_word=sorted(source_word)
# srt_target_word=sorted(target_word)

# print(srt_source_word==srt_target_word)


def anagram(word1,word2):

    return sorted(word1)==sorted(word2)

source_word="listen"

target_word="silent"

print(anagram(source_word,target_word))