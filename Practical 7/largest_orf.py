import re

seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'
start = 'AUG'
stop = ["UAA", "UAG", "UGA"]
longet = 0

for s in re.finditer("AUG",seq):
    sp = (s.start())
    #sp refers to starting position

    for i in range(s.start(),len(seq) - 2,3):
        codon = seq[i:i+3]
        #codon is the three bases from the starting position
        
        if codon in stop:
            lengths = i - sp + 3

            if lengths > longet:
                longet = lengths
                
            break

    else:
        print("no stop codon found")

print(f"the longest ORF is {longet} bases long")