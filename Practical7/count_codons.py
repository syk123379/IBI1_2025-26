from collections import Counter
import matplotlib.pyplot as plt

STOP_CODONS = {'TAA', 'TAG', 'TGA'}
INPUT_FASTA = 'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'

target_stop = input('Enter a stop codon (TAA, TAG, or TGA): ').strip().upper()

while target_stop not in STOP_CODONS:
    target_stop = input('Invalid input. Please enter TAA, TAG, or TGA: ').strip().upper()

sequences = []
header = None
sequence_lines = []

file = open(INPUT_FASTA, 'r')

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

total_codon_counts = Counter()
genes_used = 0

for header, sequence in sequences:
    best_orf = ''

    for start in range(len(sequence) - 2):
        if sequence[start:start + 3] == 'ATG':
            for pos in range(start + 3, len(sequence) - 2, 3):
                codon = sequence[pos:pos + 3]

                if codon in STOP_CODONS:
                    if codon == target_stop:
                        candidate_orf = sequence[start:pos + 3]
                        if len(candidate_orf) > len(best_orf):
                            best_orf = candidate_orf
                    break

    if best_orf != '':
        genes_used += 1

        for pos in range(0, len(best_orf) - 3, 3):
            codon = best_orf[pos:pos + 3]
            total_codon_counts[codon] += 1

if len(total_codon_counts) == 0:
    print('No genes with an ORF ending in ' + target_stop + ' were found.')
    raise SystemExit

print('Genes used:', genes_used)
print('Codon counts upstream of', target_stop + ':')

sorted_items = sorted(total_codon_counts.items(), key=lambda item: (-item[1], item[0]))

for codon, count in sorted_items:
    print(codon + ':', count)

labels = []
sizes = []

for codon, count in sorted_items:
    labels.append(codon)
    sizes.append(count)

plt.figure(figsize=(10, 10))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title('Codon usage upstream of ' + target_stop + ' in the longest ORFs')
plt.tight_layout()

output_plot = 'codon_usage_' + target_stop + '.png'
plt.savefig(output_plot, dpi=300, bbox_inches='tight')
plt.close()

print('Pie chart saved as ' + output_plot)