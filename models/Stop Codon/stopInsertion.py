"""
#####################################################################
Identifies the read-through efficiencies that can be obtained for
possible locations for stop codon insertion

Input: file (sequence.txt) that  contains a single line of nt bases
#####################################################################
"""

# Imports regular expression library
from re import *  #blindly copying Laura's method of importing
from numpy import *

### Scoring for stop codon contexts ###
# This score is somewhat representative of read-through efficiency
# determined by Namy et al, 2001
TMV = [GGA ACA CAA TAG CAA TTA CAG, 23]

### Receive .txt file containing in-frame sequence ###
# The newlines are removed, in case the sequence is multi-lined
sequence = (line.rstrip("\n") for line in open("sequence.txt", "r"))

### Search for important codon contexts ###


# Python has a built-in re.finditr method that returns the index of matches
for pos, nt in enumerate(sequence):
    if
