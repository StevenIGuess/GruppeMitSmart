#!/usr/bin/env python3

import re, sys, os, argparse, string
import numpy as np
from random import randint
from pwgen_functions import structure_string_is_valid, \
                            structure_elements_list, \
                            randstring, \
                            word_dict_get

def password_generate(word_dict,structure):
  # to be implemented
  return

def parse_command_line(argv):
  # to be implemented
  return

def main():
  try:
    args = parse_command_line(sys.argv[1:])
  except argparse.ArgumentTypeError as err:
    sys.stderr.write('{}: {}\n'.format(sys.argv[0],err))
    exit(1)
  word_dict = word_dict_get()
  pw, choice_list = password_generate(word_dict,args.structure)
  print('number of possible passwords of structure {}: {:.2e}'
         .format(args.structure,np.prod(choice_list)))
  for _ in range(args.number):
    pw, _ = password_generate(word_dict,args.structure)
    print('{}'.format(pw))

if __name__ == '__main__':
  main()
