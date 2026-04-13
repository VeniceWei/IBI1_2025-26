def protein_mass(protein):
    mass_table = {
        "G": 57.02,
        "A": 71.04,
        "S": 87.03,
        "P": 97.05,
        "V": 99.07,
        "T": 101.05,
        "C": 103.01,
        "I": 113.08,
        "L": 113.08,
        "N": 114.04,
        "D": 115.03,
        "Q": 128.06,
        "K": 128.09,
        "E": 129.04,
        "M": 131.04,
        "H": 137.06,
        "F": 147.07,
        "R": 156.10,
        "Y": 163.06,
        "W": 186.08
    }
    
    for b in protein:
        if b not in mass_table:
            raise ValueError(f"Invalid amino acid '{b}' in protein sequence.")
    total_mass = sum(mass_table[b] for b in protein)
    return total_mass

example_protein = "GASPVTC"
mass = protein_mass(example_protein)
print(f"The mass of the protein '{example_protein}' is: {mass}")