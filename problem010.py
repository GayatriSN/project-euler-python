'''
Created on 07-Jun-2016

@author: Gayatriveera
'''

sieve = [2]
i = 3
n = len(sieve) - 1 
while(sieve[n] < 2000000):
    flag = 1
    for element in sieve:
        if i % element == 0:
            flag = 0
            break
    if flag:
        #print(i)
        sieve.append(i)
        n = n + 1
    i = i + 1

print(sum(sieve)-sieve[n])