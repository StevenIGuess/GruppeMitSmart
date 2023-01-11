#!/usr/bin/env python3

import re, sys, os, argparse, string
import numpy as np
from random import randint
from pwgen_functions import structure_string_is_valid, \
                            structure_elements_list, \
                            randstring, \
                            word_dict_get

def password_generate(word_dict,structure):
  if not structure_string_is_valid(structure):
    sys.stderr.write("Please enter a valid structure string.\n")
    sys.exit(2)
  el_list=structure_elements_list(structure)
  pw=""
  choice_list=[]
  for els in el_list:
    if els[0]=="w":
      if els[1] not in word_dict:
        sys.stderr.write("There is no word of the given length.\n")
        exit(1)
      length=len(word_dict[els[1]])
      pw+=word_dict[els[1]][randint(0,length)]
      choice_list.append(length)
    else:
      pw+=randstring(string.digits if els[0]=="d" else string.punctuation, els[1])
      choice_list.append((10 if els[0]=="d" else len(string.punctuation))**els[1])
  return (pw,choice_list)
def parse_command_line(argv):
  p=argparse.ArgumentParser(description=('Input the specifications of the desired password'))
  p.add_argument('-s','--structure',type=str,default="w4p2d2w5p1d1w8",help='specify password structure, default is w4p2d2w5p1d1w8')
  p.add_argument('-n','--number',type=int,default=1,help='specify number of password, default is 1')
  return p.parse_args(argv)

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
