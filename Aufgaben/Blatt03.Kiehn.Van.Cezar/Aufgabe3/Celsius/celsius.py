#!/usr/bin/env python3
     

print("# celsius\tfahrenheit")
for i in range(1, 101):
    print('{:.2f}\t{:.2f}'.format(i, (i*9)/5+32))
