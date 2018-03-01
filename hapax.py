'''

A hapax is a word which occurs only once in either the written record of a language, the works of an author, or in a single text.
Define a function that given the file name of a text will return all its hapaxes. Make sure your program ignores capitalization.

'''

def hapax(file_path):

    words = []
    hapaxes = []

    with open(file_path, 'r') as file:

        linesF = file.readlines()

        # Removing "\n" from the words
        [words.append(line[: -1]) for line in linesF]

        for word in words:
            if words.count(word) == 1:
                hapaxes.append(word)

        return hapaxes

file_path = 'hapax.txt'
print(hapax(file_path))


