import re
import matplotlib.pyplot as plt

f = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
data = f.read()
f.close()


records = data.split('>')[1:]

while True:
    target_sc = input("Enter the stop condon(TAA/TAG/TGA):")
    if target_sc in ["TAA", "TAG", "TGA"]:
        break
    else:
        print("Error!Only input TAA, TAG or TGA\n")
#record every valid codons
all_codons = []

for item in records:
    lines = item.split('\n', 1)
    if len(lines) < 2:
        continue
    seq = lines[1].replace('\n', '').strip()
    
    codon_segments = re.findall(f'ATG(.*?){target_sc}', seq)
    
    #Retain only the longest ORF fragment in this gene
    if codon_segments:
        longest_segment = max(codon_segments, key=len)
        for i in range(0, len(longest_segment), 3):
            codon = longest_segment[i:i+3]
            if len(codon) == 3:
                all_codons.append(codon)
#count the number of codons
codon_count = {}
for codon in all_codons:
    if codon in codon_count:
        codon_count[codon] += 1
    else:
        codon_count[codon] = 1


print("Counts of in-frame codons upstream of the stop codon", target_sc)

if codon_count:
    for codon, count in codon_count.items():
        print(f"{codon}:{count}")
else:
    print("No valid codons found")

#pie chart generation
if codon_count:
    plt.figure
    plt.pie(codon_count.values(), labels=codon_count.keys(), )
    plt.title("Codon Distribution Upstream of Stop Codon:"+ target_sc)
   
    plt.savefig(f'codon_distribution_{target_sc}.png')
    plt.close()
    print(f"\nPie chart saved as: codon_distribution_{target_sc}.png")