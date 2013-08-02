'''
Created on Jul 25, 2013

@author: GRMSJAC6
'''

from mat import Mat
from vec import Vec
from GF2 import one
D=[list(range(4)),list(range(3))]

M=Mat(D,{(i,j):10*i+j for i in D[0] for j in D[1]})

V1=Vec(list(range(4)),{x:x for x in range(4)})
V2=Vec(list(range(3)),{x:x for x in range(3)})

print(V1*M)

print(M*V2)
