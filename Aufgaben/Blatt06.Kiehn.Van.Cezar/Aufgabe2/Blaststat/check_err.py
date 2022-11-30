#!/usr/bin/env python3

from mysubprocess import mysubprocess_expect

mysubprocess_expect('./blaststat.py',1,
                    "Usage: ./blaststat.py <inputfile>")
mysubprocess_expect('./blaststat.py xxx',1,
                    ("./blaststat.py: [Errno 2] No such file or "
                     "directory: 'xxx'")
