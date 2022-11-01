#!/usr/bin/env python3

import re, sys

if len(sys.argv) != 2:
  sys.stderr.write('Usage: {} <filename>\n'.format(sys.argv[0]))
  exit(1)

