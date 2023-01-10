#!/usr/bin/env python3

from mysubprocess import mysubprocess_expect

mysubprocess_expect('./pwgen.py -s p',2)
mysubprocess_expect('./pwgen.py -s dp11',2)
mysubprocess_expect('./pwgen.py -s d2p1w2x',2)
mysubprocess_expect('./pwgen.py -s a2',2)
mysubprocess_expect('./pwgen.py -s w20',1)
