import math
import itertools

max = 500

sqrs = [x*x for x in range(1,max)] 

for triplet in itertools.combinations(sqrs, 3):
    if triplet[0]+triplet[1] == triplet[2] or triplet[1]+triplet[2]==triplet[0] or triplet[2]+triplet[0]== triplet[1]:
        if sum(int(math.sqrt(x)) for x in triplet) == 1000:
            print triplet
            print math.sqrt(triplet[0]*triplet[1]*triplet[2])
            break
