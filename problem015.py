'''
Created on 07-Jun-2016

@author: Gayatriveera
'''

import math

m = 20 #Rows
n = 20 #Columns

ans = math.factorial(m + n)/( math.factorial(n) * math.factorial(m) )

print(ans)