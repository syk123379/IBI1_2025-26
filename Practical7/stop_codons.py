stop_codons = {'TAA', 'TAG', 'TGA'}
input_fasta = 'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
output_fasta = 'stop_genes.fa'

sequences = []
header = None
sequence_lines = []

file = open(input_fasta, 'r')

for line in file:
    line = line.strip()

    if line == '':
        continue

    if line.startswith('>'):
        if header is not None:
            sequences.append((header, ''.join(sequence_lines)))
        header = line[1:]
        sequence_lines = []
    else:
        sequence_lines.append(line.upper())

if header is not None:
    sequences.append((header, ''.join(sequence_lines)))

file.close()

out_file = open(output_fasta, 'w')

for header, sequence in sequences:
    found_stop_codons = set()

    for start in range(len(sequence) - 2):
        if sequence[start:start + 3] == 'ATG':
            for pos in range(start + 3, len(sequence) - 2, 3):
                codon = sequence[pos:pos + 3]
                if codon in stop_codons:
                    found_stop_codons.add(codon)
                    break

    if len(found_stop_codons) > 0:
        gene_name = header.split()[0]

        for part in header.split():
            if part.startswith('gene:'):
                gene_name = part.split(':', 1)[1]
                break

        new_header = '>' + gene_name + ' ' + ','.join(sorted(found_stop_codons))
        out_file.write(new_header + '\n')

out_file.close()

print('Finished. Results written to ' + output_fasta)