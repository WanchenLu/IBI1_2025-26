stop = input ("please input one of three possible stop codons (TAA/TAG/TGA): ")
import re
from collections import Counter
with open('stop_genes.fa','r') as infile:
    codons = []
    def find_longest_orf(seq, stop_codon):
        longest = ""
        for frame in range(3):
            i = frame
            while i <= len(seq) - 3:
                if seq[i:i+3] == 'ATG':
                    j = i + 3
                    while j <= len(seq) - 3:
                        if seq[j:j+3] == stop_codon:
                            orf = seq[i:j+3] 
                            if len(orf) > len(longest):
                                longest = orf
                            break
                        j += 3
                i += 3
        return longest
    def show_pct(pct):
        return f'{pct:.1f}%' if pct > 1 else ''
    longest_orf = ''
    for line in infile:
        if line.startswith('>'):
            if re.search(stop,line):
                state = 'yes'
            else:
                state = 'no'
        else:
            if state == 'yes':
                longest_orf = find_longest_orf(line,stop)
                if longest_orf:
                    for i in range (0,len(longest_orf),3):
                        codon = longest_orf[i:i+3]
                        codons.append(codon)
            else:
                longest_orf = ''
    if codons:
        count = Counter(codons)
        for codon,cnt in count.most_common():
            print(f"{codon}:{cnt}")
        sort = count.most_common()
        codon_list = [item[0] for item in sort]
        count_list = [item[1] for item in sort]
        import matplotlib.pyplot as plt
        total = sum(count_list)
        labels_filtered = []
        for codon, cnt in zip(codon_list, count_list):
            pct = cnt / total * 100
            if pct > 1:
                labels_filtered.append(codon)
            else:
                labels_filtered.append('')
        sizes = count_list
        plt.figure(figsize=(14, 8))
        wedges, texts, autotexts = plt.pie(
            sizes,
            labels=labels_filtered,            
            autopct=show_pct,
            startangle=90,
            pctdistance=0.85,       
            textprops={'fontsize': 7}  
        )
        plt.legend(
            wedges,
            codon_list,
            title="Codons",
            loc="center left",
            bbox_to_anchor=(1, 0, 0.5, 1),
            ncol=2,
            fontsize=6,
            title_fontsize=7
        )
        plt.axis('equal')
        plt.title("The distribution of all in-frame codons", fontsize=12,pad=20)
        plt.tight_layout()          
        plt.savefig('codon_usage.png', dpi=150)  
        plt.close()
    else:
        print("can't find ORF")