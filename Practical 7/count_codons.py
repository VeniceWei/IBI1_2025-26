import re
import matplotlib.pyplot as plt

stop_codon = str(input("input one of three possible stop codons(TAA,TAG,TGA): "))

while stop_codon not in ["TAA", "TAG", "TGA"]:
    print("Invalid input. Please enter one of the following stop codons: TAA, TAG, TGA.")
    stop_codon = str(input("input one of three possible stop codons(TAA,TAG,TGA): "))

def read_fasta(filename):
    sequences = {}
    current_name = None
    current_seq = []

    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            if line.startswith(">"):
                if current_name is not None:
                    sequences[current_name] = "".join(current_seq)

                name = line.split()[0][1:]
                current_name = name
                current_seq = []
            else:
                current_seq.append(line)

        if current_name is not None:
            sequences[current_name] = "".join(current_seq)

    return sequences

filename = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
gene_sequences = read_fasta(filename)
print(len(gene_sequences))

codon_counts = {}

for gene_name, sequence in gene_sequences.items():
    longest = 0
    true_sp = None
    for s in re.finditer("ATG", sequence):
        sp = s.start()

        for i in range(sp,len(sequence) - 2,3):
            codon = sequence[i:i+3]
            if codon == stop_codon:
                lengths = i - sp + 3
                               
                if lengths > longest:
                    longest = lengths
                    true_sp = sp
                
                break
    if longest > 0:
        print(f"{gene_name} {longest}")
        
        for i in range(true_sp, true_sp + longest - 2, 3):
                codon = sequence[i:i+3]
                if codon not in codon_counts:
                    codon_counts[codon] = 1
                else:
                    codon_counts[codon] += 1
                    #print(f"{codon}: {codon_counts[codon]}")
               

labels = list(codon_counts.keys())
values = list(codon_counts.values())

plt.figure(figsize=(23,23))
plt.title('Codon Usage Upstream of Stop Codon')
plt.pie(values, labels=labels, autopct='%.1f%%')
plt.savefig('codon_usage_pie_chart.png')
plt.close()