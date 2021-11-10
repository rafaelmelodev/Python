#!/bin/python3

import math
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

# Get the text from matrix
text = [line[i] for i in range(m) for line in matrix]
text = ''.join(text)
# Find and replace
pattern = r'([A-Za-z0-9])[!@#$%&\s]+(?=[A-Za-z0-9])'
text = re.sub(pattern,r'\1 ', text)
print(text)

# First: ([A-Za-z0-9]), the "()" capture the match as a group (useful to reuse the match later) and [A-Za-z0-9] means any character alphanumeric.
# Second: [!@#$%&\s]+ means match any symbol between square braces (the \s refers to any spacing character) one or more times.
# Third: match any alphanumeric character but not consume strings. This means, when the pattern match the position for nexts matches do not take this into account.
# So, the next line text = re.sub(pattern,r'\1 ', text) means find the pattern in text, and replace the match for the first group matched in the pattern (r'\1), which is the First between parenthesis.