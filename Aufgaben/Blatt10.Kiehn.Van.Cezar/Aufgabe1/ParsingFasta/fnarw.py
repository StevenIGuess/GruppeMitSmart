#!/usr/bin/env python3
#lst{fnarw}
from multiseq import Multiseq
from print_sequence import print_sequence
from dna2aa import dna2peptide

multiseq = Multiseq('sample.fna')
dna = multiseq[0].sequence
peptide = dna2peptide(dna)
print_sequence(peptide,60)
#lstend#
