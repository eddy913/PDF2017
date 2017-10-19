#!/usr/bin/env python3
import sys
dna_seq = sys.argv[1].upper()

ecoRI_seq = "GAATTC"
ecoRI_num = dna_seq.count(ecoRI_seq)
print("{} EcoRI  site(s) found in the sequence.".format(ecoRI_num))

if ecoRI_num == 1:
	ecoRI_loc = dna_seq.find(ecoRI_seq) + 1
	print("EcoRI site starts at postion {}.".format(ecoRI_loc))
	print("EcoRI site located at between postion {} and {}.".format(ecoRI_loc, ecoRI_loc+len(ecoRI_seq)-1))


