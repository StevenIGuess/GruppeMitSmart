#!/bin/env python3
import sys, re
#sys.argv.append("chronik_der_BRD_orig.txt")
month_list = ['Januar',
              'Februar',
              'März',
              'April',
              'Mai',
              'Juni',
              'Juli',
              'August',
              'September',
              'Oktober',
              'November',
              'Dezember']
month_dict=dict()
def fixLength(str,length,char='0'):
    while len(str)<length:
        str=char+str
    return str
for num, month in enumerate(month_list):
    month_dict[month]=fixLength(str(num+1),2)

def changeLine(line):
    ex=r"(\d{1,2}).\s*("+'|'.join(month_list)+r")\s+(\d{4})"
    #print(ex)
    for res in re.findall(ex,line):
        formattedString=f"{fixLength(res[0],2)}.{month_dict[res[1]]}.{res[2]}"
        line=re.sub(ex,formattedString,line,1)
    return line
if len(sys.argv)!=2:
    sys.stderr.write(f"Benutzung: {sys.argv[0]} <Dateiname>")
    sys.exit(1)

with open(sys.argv[1]) as stream:
    for line in stream.readlines():
        print(changeLine(line),end="")