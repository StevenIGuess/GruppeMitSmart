#!/usr/bin/env python3

import sys, string

def reverse(seq):
  return ''.join(reversed(seq))

#lst{reversecomplement}
def reverse_complement(seq):
  revcom = reverse(seq)
  transtab = str.maketrans('ACGTacgt','TGCAtgca')
  return revcom.translate(transtab)
#lstend#

if __name__ == '__main__':
  seq = 'ACTATCAGCATACT'
  print('rev_comp({})={}'.format(seq,reverse_complement(seq)))
