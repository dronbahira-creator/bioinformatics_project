def validate_dna(sequence):
    sequence = sequence.upper()
    valid = set("ATCG")

    for base in sequence:
        if base not in valid:
            return False

    return True


def transcribe_dna(sequence):
    """Transcribes DNA to RNA by replacing T with U."""
    seq_upper = sequence.upper()
    return seq_upper.replace("T", "U")


def reverse_complement(sequence):
    sequence = sequence.upper()
    comp = {"A": "T", "T": "A", "C": "G", "G": "C", "N": "N"}
    result = ""

    for base in sequence:
        result += comp.get(base, "N")

    return result[::-1]
