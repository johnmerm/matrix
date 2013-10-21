from orthogonalization import orthogonalize
from math import sqrt
from matutil import *


def orthonormalize(L):
    '''
    Input: a list L of linearly independent Vecs
    Output: A list T of orthonormal Vecs such that for all i in [1, len(L)],
            Span L[:i] == Span T[:i]
    '''
    return [(1/sqrt(l*l))*l for l in orthogonalize(L)]


def aug_orthonormalize(L):
    '''
    Input:
        - L: a list of Vecs
    Output:
        - A pair Qlist, Rlist such that:
            * coldict2mat(L) == coldict2mat(Qlist) * coldict2mat(Rlist)
            * Qlist = orthonormalize(L)
    '''
    Q = orthonormalize(L)
    Lmat = coldict2mat(L)
    Qmat = coldict2mat(Q)

    Rmat = Qmat.transpose()*Lmat

    R = mat2coldict(Rmat)

    return (Q,list(R.values()))
