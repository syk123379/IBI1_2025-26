seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'

stop_codons = {'UAA', 'UAG', 'UGA'}
largest_orf = ''

for start in range(len(seq) - 2):
    if seq[start:start + 3] == 'AUG':
        for pos in range(start + 3, len(seq) - 2, 3):
            codon = seq[pos:pos + 3]
            if codon in stop_codons:
                current_orf = seq[start:pos + 3]
                if len(current_orf) > len(largest_orf):
                    largest_orf = current_orf
                break

if largest_orf:
    print('Largest ORF:', largest_orf)
    print('Length:', len(largest_orf))
else:
    print('No complete ORF found.')