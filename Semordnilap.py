'''

A semordnilap is a word or phrase that spells a different word or phrase backwards.
("Semordnilap" is itself "palindromes" spelled backwards.) Write a semordnilap recogniser that accepts a file name
(pointing to a list of words) from the user and finds and prints all pairs of words that are semordnilap to the screen.
For example, if "stressed" and "desserts" is part of the word list, the the output should include the pair "stressed desserts".

'''

def semordnilap(file_path):

    pairs = []

    with open(file_path) as f:
        lines = []
        linesF = f.readlines()

        # Removing "\n" from the words
        [lines.append(line[: -1]) for line in linesF]

        for line in lines:
            l = len(line)
            rev = ''
            # Reversing the word
            for i in range(l - 1, -1, -1):
                rev += line[i]
            if rev in lines and rev != line:
                pairs.append(line + ' ' + rev)
                lines.remove(line)
                lines.remove(rev)
            del rev

    return pairs

file_path = 'semordnilap.txt'
print(semordnilap(file_path))
