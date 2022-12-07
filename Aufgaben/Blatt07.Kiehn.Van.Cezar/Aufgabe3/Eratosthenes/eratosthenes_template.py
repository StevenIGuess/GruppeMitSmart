#!/usr/bin/env python3
import math, sys

def usage_exit(exit_code):
  sys.stderr.write('Usage: {} <integer >= 3>\n'
                    .format(sys.argv[0]))
  exit(exit_code)

if len(sys.argv) != 2:
  usage_exit(1)

'''
Implement the Algorithm 'Sieve of Eratosthenes' in the following
function, whose header and first line is given.  In the first
line the list marked is initialized, as described in the
exercise sheet. As long as necessary, each iteration takes the
next unmarked number and marks all proper multiples of that
number. After the marking process has finished, create an empty
list prime_list and add all unmarked numbers, i.e. all
i, 2<=i<=n, such that marked[i] is False. This is the list of
prime numbers, which is returned by the function.
'''

def prime_list_by_eratosthenes(n):
  marked = [None,None] + ([False] * (n-1))
 # add your code hear

try:
  n = int(sys.argv[1])
except:
  usage_exit(2)

if n <= 2:
  usage_exit(3)

prime_list = prime_list_by_eratosthenes(n)
num_primes = len(prime_list)
print('there are {} prime numbers <= {}'.format(num_primes,n))
show_primes = 10
print('the largest {} prime numbers <= {} are:'
      .format(min(num_primes,show_primes),n))
for p in prime_list[max(0,num_primes - show_primes):]:
  print('{}'.format(p))
