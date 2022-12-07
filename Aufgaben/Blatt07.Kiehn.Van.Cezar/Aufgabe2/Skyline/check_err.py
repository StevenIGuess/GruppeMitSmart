#!/usr/bin/env python3

from mysubprocess import mysubprocess_expect

mysubprocess_expect('./skyline.py',1,None)
mysubprocess_expect('./skyline.py 1 2 3',1,None)
mysubprocess_expect('./skyline.py 1 i',1,None)
mysubprocess_expect('./skyline.py i 5',1,None)
mysubprocess_expect('./skyline.py i j',1,None)
mysubprocess_expect('./skyline.py 1 27',1,None)
mysubprocess_expect('./skyline.py 27 26',1,None)
