'''
Created on 07-Jun-2016

@author: Gayatriveera
'''

import sieve as s

num_of_div = 500
n = 0
m = 1
while m < num_of_div:
    n = n + 1
    print(n)
    sum_of_n = int((n * (n + 1))/2)
    m = s.no_of_divisors(sum_of_n)
    print(m)
print(n)