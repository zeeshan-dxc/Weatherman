"""
def get_second_half(lst):
    halfway = (int)(len(lst) / 2)
    print(type(halfway))
    second_half = lst[halfway:]
    return second_half


myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

res = get_second_half(myList)
# print(res)

print("ALL_POSSIBLE_CODONS_MADE_UP_OF_THREE_DIFFERENT_NUCLEOTIDES-----------------\n***************************\n")
possibleVals = ['A', 'C', 'G', 'T']
codons = [(x, y, z)
          for x in possibleVals for y in possibleVals for z in possibleVals]

# (A,C,G) ,(A,C,T), (A,G,C), (A,G,T), (A,T,G), (A,T,C),
# (C,G,T), (C,G,A), (C,T,A), (C,T,G), (C,A,G), (C,A,T)
# etc.


FOR X IN POSSIBLEVALS PRODUCES: 4^2 RESULTS
('A', 'A', 'A'), ('A', 'A', 'C'), ('A', 'A', 'G'), ('A', 'A', 'T'), ('A', 'C', 'A'), ('A', 'C', 'C'), ('A', 'C', 'G'), 
('A', 'C', 'T'), ('A', 'G', 'A'), ('A', 'G', 'C'), ('A', 'G', 'G'), ('A', 'G', 'T'), ('A', 'T', 'A'), ('A', 'T', 'C'), 
('A', 'T', 'G'), ('A', 'T', 'T')

print(codons)
"""

from enum import IntEnum
from typing import Tuple, List

Nucleotide: IntEnum = IntEnum('Nucleotide', ('A', 'C', 'G', 'T'))
# IntEnum gives us comparison operators 'for free', such as <, >=, and so on...
# This is necessary for the search algorithms I'll be using to work

# Codons can be defined as a tuple of three nucleotides
Codon = Tuple[Nucleotide, Nucleotide, Nucleotide]  # type alias for codons
# A gene may be defined as a list of codons
Gene = List[Codon]  # tye alias for genes

# genes on the internet will be in a file format that contains a giant string representing all the nucleotides in the gene's sequence.

# let's define an imaginary gene
gene_str: str = "ACGTGGCTCTCTAACGTACGTACGTACGGGGTTTATATATACCCTAGGACTCCCTTT"

# We also need a utility function to convert a str into a Gene


def string_to_gene(s: str) -> Gene:
    gene: Gene = []
    for i in range(0, len(s), 3):
        if (i + 2 >= len(s)):
            return gene
        codon: Codon = (Nucleotide[s[i]],
                        Nucleotide[s[i+1]], Nucleotide[s[i+2]])
        gene.append(codon)
    return gene


my_gene: Gene = string_to_gene(gene_str)

print(my_gene)
