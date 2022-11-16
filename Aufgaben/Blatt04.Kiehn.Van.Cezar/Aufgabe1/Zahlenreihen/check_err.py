#!/usr/bin/env python3

import sys, argparse
from mysubprocess import mysubprocess_expect

def parse_arguments(argv):
  p = argparse.ArgumentParser(description=('check that program handles error '
                                           'cases appropriately'))
  p.add_argument('program_path',type=str,help='specify program path')
  return p.parse_args(argv)

args = parse_arguments(sys.argv[1:])

mysubprocess_expect(args.program_path,1,
                    'Usage: {} <k>'.format(args.program_path))
mysubprocess_expect('{} abc'.format(args.program_path),1,
                    '{}: cannot convert "abc" to int'.format(args.program_path))
mysubprocess_expect('{} -3'.format(args.program_path),1,
                    '{}: parameter -3 is not positive int'
                     .format(args.program_path))
