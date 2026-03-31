import re

# --------------------- 1. 设置 ---------------------
# 终止密码子（DNA 版本：TAA, TAG, TGA）
stop_codons = {"TAA", "TAG", "TGA"}

# 输入输出文件名
input_fasta = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
output_fasta = "stop_genes.fa"

# --------------------- 2. 读取 FASTA ---------------------
def read_fasta(filename):
    """读取FASTA文件，返回 基因名:序列 字典"""
    sequences = {}
    current_name = None
    current_seq = []

    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            # 以 > 开头 = 新基因的标题行
            if line.startswith(">"):
                # 先把上一个基因存起来
                if current_name is not None:
                    sequences[current_name] = "".join(current_seq)

                # 提取基因名字（提取第一个空格前的内容）
                name = line.split()[0][1:]  # 去掉 >
                current_name = name
                current_seq = []
            else:
                # 序列行，直接拼接
                current_seq.append(line)

        # 存最后一个基因
        if current_name is not None:
            sequences[current_name] = "".join(current_seq)

    return sequences

# --------------------- 3. 寻找框内终止密码子 ---------------------
def find_in_frame_stop_codons(seq):
    """
    从ATG开始，每3个碱基读取，寻找框内终止密码子
    返回：找到的终止密码子列表
    """
    stops_found = []

    # 找到所有 ATG 的起始位置
    for match in re.finditer("ATG", seq):
        start = match.start()

        # 从 ATG 开始，每3个碱基遍历
        for i in range(start, len(seq) - 2, 3):
            codon = seq[i:i+3]

            # 如果是终止密码子
            if codon in stop_codons:
                stops_found.append(codon)
                break  # 找到一个就退出这个ORF，避免重复

    # 去重
    return list(set(stops_found))

# --------------------- 4. 主程序 ---------------------
if __name__ == "__main__":
    print("Scanning FASTA file...")
    genes = read_fasta(input_fasta)

    print("Scanning for in-frame stop codons...")
    with open(output_fasta, "w") as out:
        for gene_name, seq in genes.items():
            stops = find_in_frame_stop_codons(seq)

            # 只保留至少有一个终止密码子的基因
            if len(stops) > 0:
                # 标题行：基因名 + 找到的终止密码子
                header = f">{gene_name} stops:{','.join(stops)}"
                out.write(header + "\n")
                out.write(seq + "\n")

    print(f"The output has been saved to {output_fasta}")