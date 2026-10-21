def validate_dna(sequence):
    sequence = sequence.upper()
    valid = set("ATCG")
    for base in sequence:
        if base not in valid:
            return False
    return True
