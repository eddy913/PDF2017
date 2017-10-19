#!/usr/bin/env python3

# input sequences from commend line
import sys
dna_seq = sys.argv[1]

# count AT
count_A = dna_seq.count('A')
count_T = dna_seq.count('T')
count_AT = count_A + count_T
print("This sequence has", count_AT, "AT")

# calculate GC and print a format number
GC_con =float((len(dna_seq) - count_AT)/len(dna_seq))
print('The GC content is', '{0:.2%}'.format(GC_con) )

