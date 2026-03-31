seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'
stop = {'UAA','UAG','UGA'}
current = ''
max_length = 0
for frame in range (3):
    i = frame
    while i <= len(seq) - 3:
        codon = seq [i:i+3]
        if codon == 'AUG':
            current = codon
            start = i
            j = i + 3
            while j <= len(seq) - 3:
                ORF_codon = seq [j:j+3]
                current += ORF_codon
                if ORF_codon in stop:
                    length = j + 3 - start
                    if max_length < length:
                        largest = current
                        max_length = length
                    break
                j += 3
        i += 3
print ("the largest ORF is ", largest)
print ("the length of the largest ORF in nucleotides is ", max_length)
