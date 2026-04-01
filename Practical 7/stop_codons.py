import re
input = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
sequence = ''
gene_name = ''
for line in input:
    if line.startswith('>'):
        if gene_name != '':
            stop_codons = []
            for  match in re.finditer (r'ATG(?:...)+?(TAA|TAG|TGA)',sequence):
                stop_codons.append(match.group(1))
            if stop_codons:
                content = f">{gene_name};{stop_codons}\n"
                out_file = open('stop_genes.fa', 'a')
                out_file.write(content)
                out_file.write(f"{sequence}\n")
                out_file.close()
            sequence = ''
            gene_name = re.findall (r'gene:(.+?)\s',line)
        else :
            gene_name = re.findall (r'gene:(.+?)\s',line)
    else:
        line = line.strip()
        sequence += line
stop_codons = []
for match in re.finditer (r'ATG(?:...)+?(TAA|TAG|TGA)',sequence):
    stop_codons.append(match.group(1))
if stop_codons:
    content = f">{gene_name};{stop_codons}\n"
    out_file = open('stop_genes.fa', 'a')
    out_file.write(content)
    out_file.write(f"{sequence}\n")
    out_file.close()