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
	
	ecoRI_frag1 = dna_seq[0:ecoRI_loc]
	frag1_p = 1
	ecoRI_frag2 = dna_seq[ecoRI_loc:]
	frag2_p = ecoRI_loc + 1
	# print("The fragments are:\n{}\n{}".format(ecoRI_frag1,ecoRI_frag2))
	# frag3 = "{}\t{}\t{}".format(ecoRI_frag1,frag1_p,len(ecoRI_frag1))
	# frag4 = "{}\t{}\t{}".format(ecoRI_frag2,frag2_p,len(ecoRI_frag2))
	# print(frag3,frag4,sep='\n')

frags = []
frags.append(ecoRI_frag1)
frags.append(ecoRI_frag2)
# print(frags)
print(sorted(frags,key=len,reverse=True))
