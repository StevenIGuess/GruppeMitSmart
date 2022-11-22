#!/usr/bin/env python3
from matplotlib import pyplot as plt
import sys
plt.switch_backend('agg')
x_list=[]
y_list=[]
with open(sys.argv[1]) as stream:
    for line in stream.readlines():
        values=line.split('\t')
        x_list.append(values[0])
        y_list.append(values[1])
fig, ax=plt.subplots(figsize=(3,2))
ax.set_xticks([])
ax.set_yticks([])
for side in ['left','top','bottom','right']:
    ax.spines[side].set_visible(False)
ax.scatter(x_list,y_list,s=10,color='#E8BEAC')
fig.savefig('scatter_plot.pdf')
