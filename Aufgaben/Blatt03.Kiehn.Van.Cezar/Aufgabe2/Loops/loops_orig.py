#!/usr/bin/env python3

n = 10

# [1] convert to while loop:
print("==== 1 =====")
for i in range(1, n, 3):
  print(i)

# [2] convert to for loop:
print("==== 2 =====")
i = 0
j = n
while i < j:
  print(i, j)
  i += 1
  j -= 1

# [3] convert to while loop:
print("==== 3 =====")
for i in range(n, -n, -1):
  print(i)

# [4] convert to for loop:
print("==== 4 =====")
i = 1
while True:
  print(i)
  i += 1
  if i > n:
    break
