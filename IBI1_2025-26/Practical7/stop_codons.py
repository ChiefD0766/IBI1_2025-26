import re

f = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
data = f.read()
f.close()


records = data.split('>')[1:]
out = open('stop_genes.fa', 'w')

for item in records:
    lines = item.split('\n', 1)
    if len(lines) < 2:
        continue
    
    header = lines[0].strip()
    seq = lines[1].replace('\n', '').strip()
    gene = header.split()[0][1:]
    
    stop_list = []
    if re.search(r'ATG.*TAA', seq):
        stop_list.append('TAA')
    if re.search(r'ATG.*TAG', seq):
        stop_list.append('TAG')
    if re.search(r'ATG.*TGA', seq):
        stop_list.append('TGA')
    
    if stop_list:
        out.write(f'>{gene} {" ".join(stop_list)}\n{seq}\n')

out.close()
