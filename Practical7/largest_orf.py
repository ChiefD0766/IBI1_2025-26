seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'
import re

#record every AUG position
start_po = re.findall('AUG', seq)
starts = []
current = 0
for a in start_po:
    idx = seq.find('AUG', current)
    starts.append(idx)
    current = idx + 3

#stop codons
stops = ['UAA', 'UAG', 'UGA']
all_orfs = []

for start in starts:
    for i in range(start, len(seq)-2, 3):
        codon = seq[i:i+3]
        if codon in stops:
            orf = seq[start:i+3]
            all_orfs.append(orf)
            break

if not all_orfs:  
    print("No valid ORF found!")
else:
    longest = max(all_orfs, key=len)
    print("The largest ORF is:", longest)
    print("The length of that ORF in nucleotides is:", len(longest))
