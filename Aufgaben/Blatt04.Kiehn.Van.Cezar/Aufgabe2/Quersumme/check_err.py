#!/usr/bin/env python3

from mysubprocess import mysubprocess_expect

mysubprocess_expect('./quersumme.py',1,
                    'Usage: ./quersumme.py <integer>')
mysubprocess_expect('./quersumme.py 1.5',1,
                    './quersumme.py: argument "1.5" is not an integer')
mysubprocess_expect('./quersumme.py 1.0',1,
                    './quersumme.py: argument "1.0" is not an integer')
mysubprocess_expect('./quersumme.py a1',1,
                    './quersumme.py: argument "a1" is not an integer')
