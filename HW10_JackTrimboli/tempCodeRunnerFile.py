def initialLetterCount(wordList):
    dict = {}
    for words in wordList:
        if not dict.has_key(words[0]):
            dict[words[0]] = 1
        else:
            dict[words[0]] += 1
    return dict


horton = ["I", "say", "what", "I", "mean", "and", "I", "mean", "what", "I", "say"]
print(initialLetterCount(horton))