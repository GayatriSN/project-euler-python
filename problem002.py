'''
Created on 11-Sep-2014

@author: Gayatri SN
'''

total = 0
num3 = 0
num1 = 0
num2 = 1

'''
Every third number in Fibonacci sequence is even :)
'''
while(num3 < 4000000):
    num3 = num1 + num2
    num1 = num2 + num3
    if (num2 > 4000000): break
    total += num1
    num2 = num3 + num1
print(total)