#!/usr/bin/env python3

import re, sys

def read_variables(filename):
  try:
    stream = open(filename)
  except IOError as err:
    sys.stderr.write('{}: {}\n'.format(sys.argv[0],err))
    exit(1)
  # add your code here
  stream.close()
  # return value represents variable names and their values
  return varmap   

def substitute_variables(varmap,filename):
  try:
    stream = open(filename)
  except IOError as err:
    sys.stderr.write('{}: {}\n'.format(sys.argv[0],err))
    exit(1)
  # add your code here
  stream.close()

if len(sys.argv) != 3:
  sys.stderr.write('Usage: {} <patient_datei> <email_datei>\n'
                   .format(sys.argv[0]))
  exit(1)

varmapfile = sys.argv[1]
varmap = read_variables(varmapfile)
textfilename = sys.argv[2]
substitute_variables(varmap,textfilename)
