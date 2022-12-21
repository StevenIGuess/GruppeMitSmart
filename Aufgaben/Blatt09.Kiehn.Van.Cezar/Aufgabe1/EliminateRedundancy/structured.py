#!/bin/env python3
import math
x_vector = [6,7,12,14,23,41,53,60,69,72,100,90]
y_vector = [2.5,1.1,6.3,2.1,2.9,15.3,20.7,18.4,22,33,50,43]
z_vector = [1,12,18,33,78,99,65,77,81,54,78,77]
def compare(vecs):
    means=[sum(vec)/len(vec) for vec in vecs]
    prod_sum=0
    sqr_sums=[0,0]
    for values in zip(vecs[0],vecs[1]):
        diffs=[values[i]-means[i] for i in range(2)]
        sqr_sums=[sqr_sums[i]+diffs[i]**2 for i in range(2)]
        prod_sum+=diffs[0]*diffs[1]
    return prod_sum/math.sqrt(sqr_sums[0]*sqr_sums[1])
print('x_vector/y_vector: {:.5f}'.format(compare([x_vector,y_vector])))
print('x_vector/z_vector: {:.5f}'.format(compare([x_vector,z_vector])))
print('y_vector/z_vector: {:.5f}'.format(compare([y_vector,z_vector])))