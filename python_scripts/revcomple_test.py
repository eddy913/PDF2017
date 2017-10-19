#!/usr/bin/env python3
import sys
dna_seq = sys.argv[1].upper()


# code is too tense. need to simplify and make it clear
comple_seq = dna_seq.replace('A','t').replace('T','a').replace('G','c').replace('C','g')
revcomple_seq = comple_seq[::-1]

COMPLE_seq = comple_seq.upper()
REVCOMPLE_seq = revcomple_seq.upper()

# consider to optimize the format
print("Original sequence", "5'"+dna_seq+" 3'", sep='\t')
print("Complement", "5'"+COMPLE_seq+" 3'", sep='\t')
print("Reverse Complement", "5'"+REVCOMPLE_seq+" 3'", sep='\t')
