def shareOneLetter(wordList):
    dict = {}
    for word in wordList:
        # go through each word in the list
        if word not in dict:
            # if the word is not in the dictionary, add it as a key with an empty list as its value
            dict[word] = []
        for words in wordList:
            # go through the list and compare each word to the current word
            if words in dict[word]:
                continue
            for letter in words:
                # check each letter in words
                if letter in word:
                    dict[word].append(words)
                    break
    return dict


horton = ["I", "say", "what", "I", "mean", "and", "I", "mean", "what", "I", "say"]
print(shareOneLetter(horton))