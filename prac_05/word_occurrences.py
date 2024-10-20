"""
CP1404 - Prac 5
Program: Word Occurrences
Estimate: 20 minutes
Actual:   25 minutes
"""

from operator import itemgetter

text = input("Text: ")
words = text.split()

word_to_count = {}
for word in words:
    try:
        word_to_count[word] += 1
    except KeyError:
        word_to_count[word] = 1

max_length = max([len(word) for word in words])

for word, count in sorted(word_to_count.items(), key=itemgetter(1), reverse=True):
    print(f"{word:{max_length}} : {count}")

