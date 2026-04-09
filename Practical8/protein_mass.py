def calculate_protein_mass(sequence):
    """
    Input: aa_sequence, amino acid sequence string
    Returns: total protein mass 
    """
    aa_mass = {
        'G':57.02, 'A':71.04, 'S':87.03, 'P':97.05, 'V':99.07,
        'T':101.05, 'C':103.01, 'I':113.08, 'L':113.08, 'N':114.04,
        'D':115.03, 'Q':128.06, 'K':128.09, 'E':129.04, 'M':131.04,
        'H':137.06, 'F':147.07, 'R':156.10, 'Y':163.06, 'W':186.08
    }
    total = 0.0
    for aa in sequence:
        # check that all supplied amino acids are defined correctly and can be found in this table
        if aa not in aa_mass:
            print("Error: Invalid amino acid!")
            return None
        total = total + aa_mass[aa]
    return total

# Example 1: Valid sequence
mass1 = calculate_protein_mass("GAS")
print("Total protein mass of GAS:", mass1)
# Example 2: Invalid sequence
mass2 = calculate_protein_mass("GAB")
print("Total protein mass of GAB:", mass2)