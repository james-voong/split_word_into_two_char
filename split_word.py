#!/usr/bin/env python3

import sys

# Validation of arguments
if len(sys.argv) != 2:
    exit("Only give me one argument.")

word_list = sys.argv[1].split()

n = 2

word_pieces = []

for word in word_list:

    # This is called list comprehension.
    word_pieces += [(word[i:i+n]) for i in range(0, len(word), n)]

print(' '.join(word_pieces))