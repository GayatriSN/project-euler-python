'''
Created on 08-Jun-2016

@author: Gayatriveera
'''

f = open("p022_names.txt","r")
str = f.read()
print(str)

names = str.split(sep=",")
names = [name.replace('"','') for name in names]

names.sort()
print(names)

values = [sum([int(ord(letter)-64) for letter in name]) for name in names]

scores = []
for idx,value in enumerate(values):
    scores.append((idx + 1) * value)
    
print(sum(scores))