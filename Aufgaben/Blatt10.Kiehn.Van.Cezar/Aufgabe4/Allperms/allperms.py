#!/usr/bin/env python3

from math import factorial
import sys, argparse

def all_perms_rec(elems):
  if len(elems)<2:
    return [elems.copy()]
  perms=[]
  for i,el in enumerate(elems):
    elems.pop(i)
    perms_new=all_perms_rec(elems)
    for perm in perms_new:
      perm.append(el)
      perms.append(perm)
    elems.insert(i,el)
  return perms  
def all_permutations(elems):
  return all_perms_rec(elems)

def all_permutations_verify(all_perms,elems):
  assert len(all_perms)==factorial(len(elems))
  assert len(set(map(lambda x:tuple(x),all_perms)))==len(all_perms)
  assert all([set(perm)==set(elems) for perm in all_perms])

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
