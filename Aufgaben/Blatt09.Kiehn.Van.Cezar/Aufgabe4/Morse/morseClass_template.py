#!/usr/bin/env python3

import sys, argparse, re


class Morse:
  morse_code = \
  {
    'A' : '.-',
    'B' : '-...',
    'C' : '-.-.',
    'D' : '-..',
    'E' : '.',
    'F' : '..-.',
    'G' : '--.',
    'H' : '....',
    'I' : '..',
    'J' : '.---',
    'K' : '-.-',
    'L' : '.-..',
    'M' : '--',
    'N' : '-.',
    'O' : '---',
    'P' : '.--.',
    'Q' : '--.-',
    'R' : '.-.',
    'S' : '...',
    'T' : '-',
    'U' : '..-',
    'V' : '...-',
    'W' : '.--',
    'X' : '-..-',
    'Y' : '-.--',
    'Z' : '--..',
    '0' : '-----',
    '1' : '.----',
    '2' : '..---',
    '3' : '...--',
    '4' : '....-',
    '5' : '.....',
    '6' : '-....',
    '7' : '--...',
    '8' : '---..',
    '9' : '----.',
    '.' : '.-.-.-',
    ',' : '--..--',
    ' ' : '------'
  }
  morse_code2_0 = \
  {
    'A' : '..--',
    'B' : '-.-..--.',
    'C' : '.....',
    'D' : '.--.',
    'E' : '--.',
    'F' : '...-..',
    'G' : '...-.-.',
    'H' : '-.--.',
    'I' : '....-',
    'J' : '-.-..-.-',
    'K' : '-.-..-..',
    'L' : '-----',
    'M' : '-.-.-',
    'N' : '-..-',
    'O' : '-...',
    'P' : '-.-...--',
    'Q' : '-.-...-.',
    'R' : '---.',
    'S' : '..-.',
    'T' : '.---',
    'U' : '...--.',
    'V' : '-.-....-',
    'W' : '-.-.....',
    'X' : '...-.---',
    'Y' : '...-.--.',
    'Z' : '----.--',
    '0' : '----.-..',
    '1' : '-.------',
    '2' : '-.-----.',
    '3' : '-.----.-',
    '4' : '-.----..',
    '5' : '-.---.--',
    '6' : '-.---.-.',
    '7' : '-.---..-',
    '8' : '-.---...',
    '9' : '-.-..---',
    '.' : '----..',
    ',' : '----.-.-',
    ' ' : '.-.'
  }
  def __init__(self,use2_0 = False):
    self._use2_0 = use2_0
    self._morse_code_map = Morse.morse_code2_0 if use2_0 else Morse.morse_code

  def encode(self,text):
    # to be implemented using self._morse_code_map
    return
  def decode(self,morse_string):
    # to be implemented using self._morse_code_map
    return

# wave files are from
# https://drive.google.com/drive/folders/0B9hr-DdPL7utdkFLYXVXN25nZXc

def play_morse(morse_string):
  print('#!/bin/sh')
  print('OS=`uname -s`')
  print('if test "X${OS}Y" = "XDarwinY"')
  print('then')
  print('  SOUNDPLAYER=afplay')
  print('else')
  print('  if test "X${OS}Y" = "XLinuxY"')
  print('  then')
  print('    SOUNDPLAYER=aplay')
  print('  else')
  print('    echo "$0: unknown operating system ${OS}"')
  print('    exit 1')
  print('  fi')
  print('fi')
  for m in morse_string:
    assert m == '.' or m == '-'
    print('${{SOUNDPLAYER}} {}.wav'.format('dah' if m == '.' else 'dit'))

def play_morse_MS_WINDOWS(morse_string):
  for m in morse_string:
    assert m == '.' or m == '-'
    print('start {}.wav'.format('dah' if m == '.' else 'dit'))
    print('TIMEOUT /T 2')

def parse_arguments():
  p = argparse.ArgumentParser(description=('encoding text into  morse code '
                                           'and vice versa'))
  p.add_argument('--mc2_0',action='store_true',default=False,
                  help='use morse code in version 2.0')
  outputgroup = p.add_mutually_exclusive_group(required=False)
  outputgroup.add_argument('-t','--text',action='store_true',default=False,
                           help='output morse code as text')
  outputgroup.add_argument('--MS_WINDOWS',action='store_true',default=False,
                           help=('output morse code as MS_WINDOWS compatible '
                                 'list of statements'))
  outputgroup.add_argument('-d','--decode',action='store_true',default=False,
                           help=('decode given morse string, implies option '
                                 ' --mc2_0'))
  p.add_argument('string',type=str,metavar='string or filename',
                 help='specify input string or file name, - for stdin')
  args = p.parse_args()
  if args.decode:
    args.mc2_0 = True
  return args

args = parse_arguments()

mc = Morse(args.mc2_0)

inputstring = None
file_input = True
if args.string == '-':
  stream = sys.stdin
  file_input = False
else:
  try:
    stream = open(args.string)
  except IOError as err:
    inputstring = args.string
    file_input = False

if not inputstring:
  assert stream
  inputstring = stream.read().rstrip()

if file_input:
  stream.close()

if args.decode:
  text = mc.decode(inputstring)
  print(text)
else:
  morse_string = mc.encode(inputstring)
  if args.text:
    print(morse_string)
  else:
    if args.MS_WINDOWS:
      play_morse_MS_WINDOWS(morse_string)
    else:
      play_morse(morse_string)
