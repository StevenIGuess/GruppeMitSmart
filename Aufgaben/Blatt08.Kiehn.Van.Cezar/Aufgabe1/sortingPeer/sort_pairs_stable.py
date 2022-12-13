#!/usr/bin/env python3
#title	Sorting a list of pairs using itemgetter
from operator import itemgetter

#lst{SortColorsStable}
colors = [('red', 1), ('blue', 1), ('red', 2), ('blue', 2)]
print(sorted(colors,key=itemgetter(0)))
#lstend#
