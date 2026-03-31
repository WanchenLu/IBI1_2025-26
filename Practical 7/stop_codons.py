import re
input = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
for line in input:
    if line.startswith('>'):
        gene_name = re.findall (r'gene:(.+?)\s',line)
    else:
        stop_codons = re.findall (r'ATG(?:...)+?(TAA|TAG|TGA)',line)
        if gene_name and stop_codons:
            content = f"{gene_name}{stop_codons}\n"
            out_file = open('stop_genes.fa', 'a')
            out_file.write(content)
            out_file.close()