#!/usr/bin/env python3

n = 10

# [1] convert to while loop:
print("==== 1 =====")
i = 1
while i < n:
  print(i)
  i += 3

# [2] convert to for loop:
print("==== 2 =====")
j = n
for i in range(int(j//2)):    #//2, da in dem while loop i zunimmt und j abnimmt
    print(i,j-i)        #j-i, da in dem while loop j mit jeder itteration abnimmt

# [3] convert to while loop:
print("==== 3 =====")
i = n
while i > -n:
    print(i)
    i -= 1

# [4] convert to for loop:
print("==== 4 =====")
for i in range(n):
    print(i + 1)    #i + 1, da while bei 1 und for bei 0 anfängt
