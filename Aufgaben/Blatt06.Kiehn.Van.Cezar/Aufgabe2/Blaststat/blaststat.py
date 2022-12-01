#!/bin/env python3
import sys, re, math
sys.argv.append("blaststat.txt")
if len(sys.argv) == 1:
    sys.stderr.write(f"Usage: {sys.argv[0]} <iputfile>\n")
    sys.exit(1)
distScore, distLog, distIdentities=dict(),dict(),dict()
try:
    stream=open(sys.argv[1])
except IOError as err:
  sys.stderr.write('{}: {}\n'.format(sys.argv[0],err))
  exit(1)
for num,line in enumerate(stream.readlines()):
    hasFound=False
    expressions=[r"Score\s*=\s*(\d+)\sbits\s*\(\d+\),\s*Expect\s*=\s*(\de\-?"+
                 r"\d+|0\.0)", r"Identities\s*=\s*\d+\/\d+\s*\((\d+)%\)"]
    values=[]
    for ex in expressions:
        res=re.findall(ex,line)
        if len(res)>0:
            hasFound=True
        if len(res)>=1:
            if type(res[0])==tuple:
                values.extend(res[0])
            else:
                values.append(res[0])
    for i,v in enumerate(values):
        if 'e' in v:
            values[i]=round(math.log10(int(v.split('e')[0])*
                      math.pow(10,int(v.split('e')[1]))))
            if values[i] not in distLog:
                distLog[values[i]]=1
            else:
                distLog[values[i]]+=1
        elif v=='0.0':
            values[i]=0
            if values[i] not in distLog:
                distLog[values[i]]=1
            else:
                distLog[values[i]]+=1
        else:
            values[i]=int(v)
            if num%2==0:
                if values[i] not in distScore:
                    distScore[values[i]]=1
                else:
                    distScore[values[i]]+=1
            else:
                if values[i] not in distIdentities:
                    distIdentities[values[i]]=1
                else:
                    distIdentities[values[i]]+=1
    if hasFound:
        print("V",end='')
        for i,v in enumerate(values):
            print(f"\t{v}",end='')
        print()
for i,dist in enumerate([distScore,distLog,distIdentities]):
    if len(dist.values())>0:
        if i==0 and dist.values:
            print("# distribution of bitscores")
            print("# Fields: bitscore, occurrences")
        elif i==1:
            print("# distribution of log10(expect)")
            print("# Fields: log10(expect), occurrences")
        else:
            print("# distribution of identities")
            print("# Fields: identity, occurrences")
        for k in sorted(dist):
            print(f"D\t{k}\t{dist[k]}")
