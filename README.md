# Bioinformatics Project

# DNA Sequence Toolkit

## Question

Can I validate, transcribe, and reverse-complement a DNA sequence in Python?

## Methods

- `validate_dna(sequence)` — checks whether every nucleotide is a valid DNA base.
- `transcribe_dna(sequence)` — replaces T with U (DNA → RNA).
- `reverse_complement(sequence)` — generates the reverse complement of a DNA sequence.

## Results

Tested with the sequence `atcgatcg`.

Expected output:

- Valid: `True`
- RNA: `AUCGAUCG`
- Reverse complement: `CGATCGAT`

All three functions produced the expected results.

## Run

From the project root, execute:

```bash
python3 scripts/dna.py
```
