#!/usr/bin/env python3

import re
from codon2aa import codon2aa
from rev_comp import reverse_complement

#lst{dnatopeptide}
def dna2peptide(seq):
  peptide_list = list()
  for codon in re.findall(r'[acgt]{3}',seq,flags=re.I):
    peptide_list.append(codon2aa(codon))
  return ''.join(peptide_list)
#lstend#

def dna2peptide_wrong(seq):
  peptide_list = list()
  for i in  range(0,len(seq)-3):
    print('i={}'.format(i))
    codon = seq[i:i+3]
    if re.search(r'^[acgt]{3}$',codon,flags=re.I):
      peptide_list.append(codon2aa(codon))
    i += 3 # does not work as supposed, i is incremented by 1
  return ''.join(peptide_list)

if __name__ == '__main__':
  import sys
  import fastaIterator
  from print_sequence import print_sequence
  if len(sys.argv) != 2:
    sys.stderr.write('Usage: {} <filename>\n'.format(sys.argv[0]))
    exit(1)

  filename = sys.argv[1]

  for header, seq in fastaIterator.fasta_next(filename):
    peptide = dna2peptide(seq)
    print('>translation of {}'.format(header))
    print_sequence(peptide,70)
    print('>translation of {}'.format(header))
    peptide = dna2peptide(reverse_complement(seq))
    print_sequence(peptide,70)
