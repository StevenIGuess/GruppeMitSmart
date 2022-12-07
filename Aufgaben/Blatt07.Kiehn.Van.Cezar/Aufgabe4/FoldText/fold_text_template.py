#!/usr/bin/env python3

import re, sys

def usage():
  sys.stderr.write('Usage: {} <max_line_width> <inputfile>\n'
                   .format(sys.argv[0]))
  exit(1)

def fold_text(max_line_width,filename):
  try:
    stream = open(filename, 'r')
  except IOError as err:
    sys.stderr.write('{}: {}\n'.format(filename, err))
    exit(1)
# here you add your code processing each line
  stream.close()

if len(sys.argv) != 3:
  usage()

try:
  max_line_width = int(sys.argv[1])
except ValueError as err:
  sys.stderr.write('{}: cannot convert {} into integer\n'
                   .format(filename, err))
  usage()

fold_text(max_line_width,sys.argv[2])
