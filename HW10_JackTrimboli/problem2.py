def initalLetters(wordList):
    dict = {}
    for words in wordList:
        if not dict.has_key(words[0]):
            # if the dictionary does not contain the key, add it
            dict[words[0]] = []
        if words not in dict[words[0]]:
            # if the list corresponding to that key does not already contain that value, append it to the list.
            dict[words[0]].append(words)
    return dict


horton = ["I", "say", "what", "I", "mean", "and", "I", "mean", "what", "I", "say"]
print(initalLetters(horton))