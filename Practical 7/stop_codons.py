import re

stop_codons = {"TAA", "TAG", "TGA"}
input_fasta = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
output_fasta = "stop_genes.fa"

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

def find_in_frame_stop_codons(seq):
    """
    从ATG开始，每3个碱基读取，寻找框内终止密码子
    返回：找到的终止密码子列表
    """
    stops_found = []

    for match in re.finditer("ATG", seq):
        start = match.start()

        for i in range(start, len(seq) - 2, 3):
            codon = seq[i:i+3]

            if codon in stop_codons:
                stops_found.append(codon)
                break

    return list(set(stops_found))

if __name__ == "__main__":
    print("Scanning FASTA file...")
    genes = read_fasta(input_fasta)

    print("Scanning for in-frame stop codons...")
    with open(output_fasta, "w") as out:
        for gene_name, seq in genes.items():
            stops = find_in_frame_stop_codons(seq)

            if len(stops) > 0:
                header = f">{gene_name} stops:{','.join(stops)}"
                out.write(header + "\n")
                out.write(seq + "\n")

    print(f"The output has been saved to {output_fasta}")