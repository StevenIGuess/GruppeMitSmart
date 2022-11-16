#!/usr/bin/env python3
import sys
def nextValue(curr,seq,i):
    if seq==0:
        return curr/2+curr/(1+2*i)
    if seq==1:
        return curr/(-2)
    if seq==2:
        return curr/i
    if seq==3:
        return (curr*(i-1))/(2*i)
    if seq==4:
        return curr+(i-1)
def getString(v,seq):
    if seq==4:
        return str(v)
    else:
        return "{:.5e}".format(v)
values=[2.5,1,1,0.5,0]
if len(sys.argv)<2:
    sys.stderr.write(f"Usage: {sys.argv[0]} <k>")
    sys.exit(1)
try:
    k=int(sys.argv[1])
except ValueError as err:
    sys.stderr.write(f'{sys.argv[0]}: cannot convert "{sys.argv[1]}" to int')
    sys.exit(1)
if k<1:
    sys.stderr.write(f'{sys.argv[0]}: parameter {k} is not positive int')
    sys.exit(1)
for i in range(5):
    print(f"Reihe {chr(i+97)}")
    sum=values[i]
    print(getString(values[i],i))
    for j in range(2,k+1):
        values[i]=nextValue(values[i],i,j)
        print(getString(values[i],i))
        sum+=values[i]
    print(f"Summe: {getString(sum,i)}")