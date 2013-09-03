from vecutil import  *
from matutil import  *

def bit_list(i,n=3):
    return [ (i//2**k) % 2 for k in reversed(range(n)) ]
def bit_string(i,n=3):
    return ''.join([str(e) for e in bit_list(i,n)])

def bit_vec(i,n=3):
    return list2vec( bit_list(i,n))

def hardamad(n):
#     return listlist2mat([
#                   [ 1 if (bit_vec(i) * bit_vec(j)) % 2 == 0 else -1 for i in range(8) ]
#                    for j in range(8) ])
    D = 2*[{bit_string(i,n) for i in range(2**n) }]
    
    
    v = {(bit_string(i,n),bit_string(j, n)): 1 if (bit_vec(i) * bit_vec(j)) % 2 == 0 else -1 for i in range(2**n) for j in range(2**n) }

    return Mat(D,v)

def amp_hardamad(n):
    return 2**(-n/2)

print(hardamad(3))
print(amp_hardamad(3))