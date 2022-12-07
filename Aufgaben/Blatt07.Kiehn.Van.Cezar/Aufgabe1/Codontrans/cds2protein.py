#!/usr/bin/env python3
import sys, re, argparse
from codon2aa import codon2aa

def cds2protein(seq):
  aa_list = list()
  for codon in re.findall(r'[acgt]{3}',seq,flags=re.I):
    aa = codon2aa(codon)
    if aa == '*':
      break
    aa_list.append(aa)
  return ''.join(aa_list)

def parse_arguments():
  p = argparse.ArgumentParser(description=('transform coding sequence into '
                                           'protein'))
  p.add_argument('inputfile',type=str,
                  help='specify input file with coding sequence')
  return p.parse_args()

args = parse_arguments()

try:
  stream = open(args.inputfile)
except IOError as err:
  sys.stderr.write('{}: {}\n'.format(sys.argv[0],err))
  exit(1)
sequence = re.sub('\s','',stream.read())
stream.close()
protein = cds2protein(sequence)
print(protein)
