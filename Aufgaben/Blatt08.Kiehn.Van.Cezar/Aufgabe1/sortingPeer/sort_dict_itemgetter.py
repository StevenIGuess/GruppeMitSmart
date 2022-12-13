#!/usr/bin/env python3
#title	Sorting a dictionary using itemgetter

from operator import itemgetter

eop_dist = {'=' : 5, 'I' : 3, 'X' : 4, 'D' : 1}

#lst{SortedEopDictItemGetter}
for eop, count in sorted(eop_dist.items(),\
                         key=itemgetter(1),\
                         reverse=True):
  print('{}\t{}'.format(eop,count))
#lstend#
