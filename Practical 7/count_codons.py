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
for codon,cnt in count.most_common():
    print(f"{codon}:{cnt}")
sort = count.most_common()
codon_list = [item[0] for item in sort]
count_list = [item[1] for item in sort]
import matplotlib.pyplot as plt
sizes = count_list
plt.pie(sizes,labels=codon_list,autopct='%1.1f%%',startangle=90)
plt.axis('equal')
plt.title("the distribution	of all in-frame codons")
plt.savefig('codon_usage.png')
plt.close()