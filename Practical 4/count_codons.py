stop = input ("please input one of three possible stop codons (TAA/TAG/TGA): ")
import re
from collections import Counter
input = open ('stop_genes.fa','r')
codons = []
upstream = []
for line in input:
    if line.startswith('>'):
        if re.search(stop,line):
            state = 'yes'
        else:
            state = 'no'
    else:
        if state == 'yes':
            upstream.extend(re.findall(r'(ATG(?:.{3})+?)'+stop,line))
        else:
            continue
longest = max(upstream,key=len)
for i in range (0,len(longest),3):
    codon = longest[i:i+3]
    codons.append(codon)
count = Counter(codons)
for codon,count in codon_count.most_common():
    print(f"{codon}:{count}")