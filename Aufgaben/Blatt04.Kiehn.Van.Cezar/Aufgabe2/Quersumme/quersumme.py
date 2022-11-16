#!/usr/bin/env python3
import sys
import re
if len(sys.argv)<2:
    sys.stderr.write(f"Usage: {sys.argv[0]} <integer>")
    sys.exit(1)
num=sys.argv[1].replace(" ","")
if len(re.sub("[+-]?[0-9]*","",num))!=0:
    sys.stderr.write(f'{sys.argv[0]}: argument "{num}" is not an integer')
    sys.exit(1)
sum=0
for i in num.replace("+","").replace("-",""):
    sum+=ord(i)-48
print(f'{num}\t{sum}')