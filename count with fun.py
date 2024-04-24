def count_words(sentence):
    words=sentence.split()
    word_freq={}
    for word in words:
        if word in word_freq:
            word_freq[word]+=1
        else:
            word_freq[word]=1
    return word_freq
sentence=input('Enter the string')
word_frequ=count_words(sentence)
print(word_frequ)
