#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    sys.stderr.write("Usage: {} <inputfile>\n".format(sys.argv[0]))
    exit(1)


filename = sys.argv[1]

try:
    stream = open(filename, 'r')
except:
    sys.stderr.write("Could not open file '{}' \n".format(sys.argv[1]))
    exit(1)


hydrophobic_chars = ['A', 'F', 'I', 'L', 'M', 'P', 'V', 'W']
hydrophilic_chars = ['C', 'D', 'E', 'G', 'H', 'K', 'N', 'Q', 'R', 'S', 'T', 'Y']

print("# hydrophobic\thydrophilic")

for line in stream:
    hydrophobic = 0
    hydrophilic = 0

    for i in range(len(hydrophobic_chars)):
        hydrophobic += line.count(hydrophobic_chars[i])

    for i in range(len(hydrophilic_chars)):
        hydrophilic += line.count(hydrophilic_chars[i])

    print("{}\t{}".format(hydrophobic, hydrophilic))
    
    

stream.close()
