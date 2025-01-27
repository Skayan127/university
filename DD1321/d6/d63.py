# import sys

# if len(sys.argv) < 3:
#    print("parametrar saknas")
#    sys.exit()
# else:
#    print("parameter 1 är",  sys.argv[1], " och parameter 2 är", sys.argv[2])

# Rayan Alnakar, rayana@kth.se
# Project d3, DD1321 "Tillämpad programmering och datalogi"
# 2021-02-01


import sys
from queueOfWordsFile import queueOfWords
from DictHash import DictHash

class ParentNode: # Class for the nodes of the children and parents.
    def __init__(self, word, parent = None):
        self.word = word
        self.parent = parent

    def __str__(self): # Function to recursively print the way between the first and last word.
        if self.parent == None:
            return str(self.word)
        else:
            return str(self.parent) + " -> " + str(self.word)


with open("word3.txt", "r") as text_file:   # Reads the words from the file.
    data = text_file.readlines()


c = DictHash().__dict__ 
for x in range(0,len(data)):    # Adds the words to the dictionary.
    c[data[x].strip()] = 1
y = sorted(list(c)[1::])


if len(sys.argv) < 3:           # The command line argument. If the requirements are not met, an error message is printed.
    print("Start- och slutord saknas")
    print("Använd programmet så här: \n\t python3", sys.argv[0], " [startord] [slutord]")
    sys.exit()
else:

    start_word = ParentNode(sys.argv[1])    # Input from the user for the starting and ending word.
    last_word = sys.argv[2]

    p = queueOfWords()                      # Uses the queue to store words that have not been tested yet.
    p.enqueue(start_word)
    visited_children=[]
    rakna=0

    while not p.isEmpty():
        nextWord = p.dequeue()

        def makechildren(foralder): # Creates the unique children of the current word.
            unique_children=[]
            x = foralder.word
            for i in y: 

                if x[1:] == i[1:] and x != i :  # Length of every word is hard-coded to be three letters long.
                    unique_children.append(ParentNode(i,foralder)) 
                elif x[:2] == i[:2] and x !=i:
                    unique_children.append(ParentNode(i,foralder))

                elif x[0] == i[0] and x[-1] == i[-1] and x !=i:
                    unique_children.append(ParentNode(i,foralder))

            for i in unique_children:           # Adds the generated elements in unique_children to the visited_children list if they are not already there.
                if i.word not in visited_children:
                    visited_children.append(i.word)
                    p.enqueue(ParentNode(i.word,foralder)) # Adds the nodes to the queue.

                if last_word == i.word: # If a path is found, exit and print the path.
                    print(i)
                    sys.exit()
        rakna += 1
        makechildren(nextWord)
