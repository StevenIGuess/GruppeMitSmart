#!/usr/bin/env python3
#title	Sorting a dictionary by key or by value

#lst{SortDictionarybyKeys}
eop_dist = {'=' : 5, 'I' : 3, 'X' : 4, 'D' : 1}
print('sorted keys of eop_dist={}'.format(sorted(eop_dist)))
#lstend#

#lst{ValuesSortedDictKeysFunction}
def values_sorted_dict_keys(d):
  def apply_dict(k):
    return d[k]
  return sorted(d,key=apply_dict)

print('values_sorted_eop_dist_keys={}'
        .format(values_sorted_dict_keys(eop_dist)))
#lstend#

#lst{ValuesSortedDictKeysLambda}
print('values_sorted_eop_dist_keys={}'
       .format(sorted(eop_dist,key=lambda k: eop_dist[k])))
#lstend#
