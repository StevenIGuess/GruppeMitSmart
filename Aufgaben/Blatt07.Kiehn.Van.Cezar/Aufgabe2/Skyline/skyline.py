#!/bin/env python3
import sys
def skyline(i):
    skylineString=""
    for char in range(ord('a'),ord('a')+i):
        skylineString=skylineString+chr(char)+skylineString
    return skylineString
def parse_command_line(values):
    if len(values) not in [1,2]:
        sys.stderr.write(f"Usage: {sys.argv[0]} <lower bound> <upper bound>\n")
        sys.exit(1)
    try:
        values=list(map(lambda x: int(x),values))
    except ValueError as err:
        sys.stderr.write("Es müssen ganze Zahlen als Argumente angegeben werden.\n")
        sys.exit(1)
    fitting=list(map(lambda x: (x in list(range(27))),values))
    if False in fitting:
        sys.stderr.write("Es müssen positive ganze Zahlen kleiner oder gleich 26 als Argumente angegeben werden\n")
        sys.exit(1)
    if len(values)==1:
        return (values[0],values[0])
    else:
        return (values[0],values[1])
if __name__=="__main__":
    numbers=parse_command_line(sys.argv[1:])
    for i in range(numbers[0],numbers[1]+1):
        print(skyline(i))