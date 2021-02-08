import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):

    pos_k1, pos_k2 = x1 + v1, x2 + v2

    meet = False
    for j in range(1, 10000, 1):
        if pos_k1 == pos_k2:
            meet = True
            break   
        else:
            pos_k1 += v1
            pos_k2 += v2

    return "YES" if meet else "NO"

if __name__ == '__main__':

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

result = kangaroo(x1, v1, x2, v2)
print(result)