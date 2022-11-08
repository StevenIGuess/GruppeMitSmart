#!/usr/bin/env python3

num1 = 7
num2 = 8
ls1 = []
ls2 = [1,2,3]

if num1 + num2 > 15:
  print('1')

if (num1 + num2) % 2 == 0:
  print('2')

if (num1 * num2) % 16 == 0:
  print('3')

if len(ls2) == 2:
  print('4')

if len(ls1) + len(ls2) == 5:
  print('5')

if ls1 != [] and ls1[0] == ls1[len(ls1)-1]:
  print('6')
