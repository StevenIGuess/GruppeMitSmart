def getSum(summands,dist):
    sum=0
    for v,n in zip(summands,dist):
        sum+=v*n
    return sum
def removeLowest(dist):
    for i,v in enumerate(dist):
        if v>1:
            dist[i]-=1
            return dist
def splitnumber_exists(number,summands):
    # Hier wurde keine rekursive Lösung angewandt, das ist mit Prof. Kurtz
    # abgesprochen
    if number==0:
        return True
    if len(summands)==0:
        return False
    distQueue=[[]]
    dists=[]
    for i,v in enumerate(summands):
        if i==0:
            distQueue[0].append(number//v)
        else:
            distQueue[0].append(0)
    while len(distQueue)>=1:
        if getSum(summands,distQueue[0])==number:
            dist=[]
            for i,v in enumerate(distQueue[0]):
                for _ in range(v):
                    dist.append(summands[i])
            dists.append(dist)
        for i,v in enumerate(distQueue[0][:-1]):
            if v==0:
                continue
            distNew=distQueue[0].copy()
            distNew[i]-=1
            distNew[i+1]+=1
            while getSum(summands,distNew)>number:
                distNew=removeLowest(distNew)
            if distNew not in distQueue:
                distQueue.append(distNew)
        distQueue.pop(0)
    return len(dists)>0