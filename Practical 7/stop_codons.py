import re
with open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r') as input,\
    open ('stop_genes.fa', 'w') as out_file:
    sequence = ''
    gene_name = ''
    for line in input:
        if line.startswith('>'):
            if gene_name != '':
                stop_codons = []
                for codon in ['TAA','TGA','TAG']:
                    if codon in sequence:
                        stop_codons.append(codon)
                if stop_codons:
                    content = f">{gene_name};{",".join(stop_codons)}\n"
                    out_file.write(content)
                    out_file.write(f"{sequence}\n")
                sequence = ''
                gene_name = re.findall (r'gene:(.+?)\s',line)
            else :
                gene_name = re.findall (r'gene:(.+?)\s',line)
        else:
            line = line.strip()
            sequence += line
    stop_codons = []
    for codon in ['TAA','TGA','TAG']:
        if codon in sequence:
            stop_codons.append(codon)
    if stop_codons:
        content = f">{gene_name};{",".join(stop_codons)}\n"
        out_file.write(content)
        out_file.write(f"{sequence}\n")