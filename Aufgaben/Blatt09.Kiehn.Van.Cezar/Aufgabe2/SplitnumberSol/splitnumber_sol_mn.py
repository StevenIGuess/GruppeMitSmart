#!/usr/bin/env python3

import sys, argparse
from splitnumber_sol import splitnumber_sol

def parse_arguments(argv):
  p = argparse.ArgumentParser(description='Split number into summands')
  p.add_argument('number',type=int,help='specify number to be split')
  p.add_argument('terms_of_sum',nargs='+',help='specify terms of the sum')
  return p.parse_args(argv)

def convert_to_int(terms_of_sum):
  i_terms_of_sum = list()
  for arg in terms_of_sum:
    try:
      value = int(arg)
    except ValueError:
      sys.stderr.write('{}: cannot convert "{}" to integer\n'
                        .format(sys.argv[0],arg))
      exit(1)
    i_terms_of_sum.append(value)
  return sorted(i_terms_of_sum)

args = parse_arguments(sys.argv[1:])
i_terms_of_sum = convert_to_int(args.terms_of_sum)

solutions = splitnumber_sol(args.number,i_terms_of_sum)
print('({},[{}],{})'.format(args.number,', '.join(args.terms_of_sum),
                            solutions))
