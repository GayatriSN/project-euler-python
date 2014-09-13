'''
Created on 08-Sep-2014

@author: Gayatri SN

PROBLEM 1: Find the sum of all the multiples of 3 or 5 below 1000.
'''

from math import floor

start = 1
end = 999

threes = (floor(end/3)/2)*(3+(floor(end/3)*3))
#print(threes)

fives = (floor(end/5)/2)*(5+(floor(end/5)*5))
#print(fives)

fifteens = (floor(end/15)/2)*(15+(floor(end/15)*15))
#print(fifteens)

total = floor(threes + fives - fifteens)

print(total)