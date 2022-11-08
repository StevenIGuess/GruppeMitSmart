#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    sys.stderr.write("Usage: {} <inputfile>\n".format(sys.argv[0]))
    exit(1)

filename = sys.argv[1]

try:
    with open(filename, 'r') as stream:
        hydrophobic_chars = ['A', 'F', 'I', 'L', 'M', 'P', 'V', 'W']
        hydrophilic_chars = ['C', 'D', 'E', 'G', 'H', 'K', 'N', 'Q', 'R', 'S', 'T', 'Y']

        print("# hydrophobic\thydrophilic")

        for line in stream:
            [hydrophobic, hydrophilic] = [0, 0]

            for c in line:
                if c in hydrophobic_chars:
                    hydrophobic+=1
                elif c in hydrophilic_chars:
                    hydrophilic+=1

            print("{}\t{}".format(hydrophobic, hydrophilic))
except:
    sys.stderr.write("Could not open file '{}' \n".format(sys.argv[1]))
    exit(1)