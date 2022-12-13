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
  if number==0:
    return True
  if len(summands)==0:
    return False
  distQueue=[[]]
  for i,v in enumerate(summands):
    if i==0:
      distQueue[0].append(number//v)
    else:
      distQueue[0].append(0)
  while getSum(summands,distQueue[0])!=number:
    for i,v in enumerate(distQueue[0][:-1]):
      if v==0:
        continue
      distNew=distQueue[0].copy()
      distNew[i]-=1
      distNew[i+1]+=1
      while getSum(summands,distNew)>number:
        distNew=removeLowest(distNew)
      if getSum(summands,distNew)==0:
        continue
      if distNew not in distQueue:
        distQueue.append(distNew)
    if len(distQueue)>1:
      distQueue.pop(0)
    else:
      break
  return getSum(summands,distQueue[0])==number