word = input('Enter the name')
word_length = len(word)

for i in range(word_length):
    for j in range(word_length):
        if i == j or i == word_length - j - 1:
            print(word[i], end="")
        else:
            print(" ", end="")
    print()