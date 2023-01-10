import re, sys, os
from random import randint

def structure_string_is_valid(structure_string):
  if re.search(r'^([dpw][1-9]\d*)+$',structure_string):
    return True
  return False

def structure_elements_list(structure_string):
  sel = list()
  for mo in re.finditer(r'([dpw])([1-9]\d*)',structure_string):
    sel.append((mo.group(1), int(mo.group(2))))
  return sel

def randstring(alphabet,num):
  alpha_size = len(alphabet)
  return ''.join([alphabet[randint(0,alpha_size-1)] \
                  for _ in range(num)])

# as we want to use pwgen.py from anywhere, we use the absolute path
# of this file, determine the parent directory, in which the file
# wordlist.txt is found. The students are not required to do it in
# this way and can assume that wordlist.txt is in the local directory.

def word_dict_get():
  this_dir = os.path.dirname(os.path.abspath(__file__))
  try:
    stream = open('{}/wordlist.txt'.format(this_dir))
  except IOError as err:
    sys.stderr.write('{}: {}\n'.format(sys.argv[0],err))
    exit(1)
  word_dict = dict()
  for word in stream:
    word = word.rstrip()
    if not len(word) in word_dict:
      word_dict[len(word)] = list()
    word_dict[len(word)].append(word.lower())
  stream.close()
  return word_dict
