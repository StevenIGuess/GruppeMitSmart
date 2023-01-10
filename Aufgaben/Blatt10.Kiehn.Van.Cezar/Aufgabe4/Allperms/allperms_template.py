#!/usr/bin/env python3

from math import factorial
import sys, argparse

def all_permutations(elems):
  # to be implemented
  return

def all_permutations_verify(all_perms,elems):
  # to be implemented
  return

def parse_command_line(argv):
  p = argparse.ArgumentParser(description='generate and verify permutations')
  p.add_argument('setsize',type=int, help='specify size of set to permute')
  return p.parse_args(argv)

def main():
  args = parse_command_line(sys.argv[1:])
  elems = list(range(args.setsize))
  all_perms = all_permutations(elems)
  all_permutations_verify(all_perms,elems)

if __name__ == '__main__':
  main()
