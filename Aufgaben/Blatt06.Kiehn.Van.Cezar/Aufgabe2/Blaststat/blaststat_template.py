#!/usr/bin/env python3

import sys, re
from math import log10


if len(sys.argv) != 2:
  sys.stderr.write('Usage: {} <inputfile>\n'.format(sys.argv[0]))
  exit(1)

inputfile = sys.argv[1]
try:
  stream = open(inputfile)
except IOError as err:
  sys.stderr.write('{}: {}\n'.format(sys.argv[0],err))
  exit(1)

