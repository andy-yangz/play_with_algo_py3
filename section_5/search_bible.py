import string
from BST import BST
import time
from collections import Counter


def preprocess(lines):
    words = []
    for line in lines:
        line = line.strip()
        clean = line.translate(str.maketrans('', '', string.punctuation))
        words.extend([word.lower() for word in clean.split(" ")])
    return words

lines = open("bible.txt").readlines()
words = preprocess(lines)
print(f"Totally {len(words)} words.")

bst = BST()

for word in words:
    if bst.contain(word):
        node = bst.search(word, get_node=True)
        node.value += 1
    else:
        bst.insert(word, 1)

start = time.time()
print(f"Contain god {bst.search('god')} times.")
print(f"Cost {time.time()-start} secs.")

counter = Counter(words)
start = time.time()
print(f"Contain god {counter['god']} times.")
print(f"Cost {time.time()-start} secs.")