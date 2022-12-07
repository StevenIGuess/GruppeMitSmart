#!/usr/bin/env python3

import re, sys
#sys.argv.append(70)
#sys.argv.append("Aufgabe4/FoldText/python_history.txt")
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
  for line in stream.readlines():
    text=line.split(" ")
    if len(text)>1:
      width_curr=len(text[0])
      print(f"{text[0]}",end='')
      for word in text[1:]:
        if(word[-1]=='\n'):
          word=word[:-1]
        if width_curr+len(word)+1>max_line_width:
          print()
          print(word,end='')
          width_curr=len(word)
        else:
          print(f" {word}",end='')
          width_curr+=(len(word)+1)
    print()

# here you add your code processing each line
  stream.close()

if len(sys.argv) != 3:
  usage()

try:
  max_line_width = int(sys.argv[1])
except ValueError as err:
  sys.stderr.write('{}: cannot convert {} into integer\n'
                   .format(sys.argv[1], err))
  usage()

fold_text(max_line_width,sys.argv[2])