'''
Created on 14-Sep-2014

@author: Gayatriveera
'''

import math

num = 600851475143

while (num % 2 == 0):
    num = num // 2

prime = 3

while (prime <= num):
    while (num % prime == 0):
        num = num // prime
    flag = 0
    i = prime + 2
    while (i <= num and flag == 0):
        j = 3
        flag = 1
        while ( j <= int(math.sqrt(i))+1 and flag > 0):
            flag = j % i
            j = j + 1
        if (flag > 0):
            prime = i
        i = i + 2
print(prime)