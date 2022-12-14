#!/usr/bin/env python3

import re, sys

def read_variables(filename):
  try:
    stream = open(filename)
  except IOError as err:
    sys.stderr.write('{}: {}\n'.format(sys.argv[0],err))
    exit(1)
  # add your code here
  varmap=dict()
  for line in stream.readlines():
    res=re.search(r"^(_[A-Z]+_)\t(.+)\n$",line)
    varmap[res.group(1)]=res.group(2)
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
  for line in stream.readlines():
    for match in re.findall(r"\w+|\W+",line):
      if re.match(r"_[A-Z]+_",match):
        print(varmap[match],end="")
      else:
        print(match,end="")
  stream.close()

if len(sys.argv) != 3:
  sys.stderr.write('Usage: {} <patient_datei> <email_datei>\n'
                   .format(sys.argv[0]))
  exit(1)

varmapfile = sys.argv[1]
#varmapfile = "Aufgabe2/FormEmail/patient1.tsv"
varmap = read_variables(varmapfile)
textfilename = sys.argv[2]
#textfilename = "Aufgabe2/FormEmail/email_generisch.txt"
substitute_variables(varmap,textfilename)
