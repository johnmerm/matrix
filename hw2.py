# version code 761
# Please fill out this stencil and submit using the provided submission script.

from vec import Vec



## Problem 1
def vec_select(veclist, k): 
    '''
    >>> D = {'a','b','c'}
    >>> v1 = Vec(D, {'a': 1})
    >>> v2 = Vec(D, {'a': 0, 'b': 1})
    >>> v3 = Vec(D, {        'b': 2})
    >>> v4 = Vec(D, {'a': 10, 'b': 10})
    >>> vec_select([v1, v2, v3, v4], 'a') == [Vec(D,{'b': 1}), Vec(D,{'b': 2})]
    True
    '''
    from vec import getitem
    return [ v for v in veclist if v[k] == 0 ]

D = {'a','b','c'}
v1 = Vec(D, {'a': 1})
v2 = Vec(D, {'a': 0, 'b': 1})
v3 = Vec(D, {        'b': 2})
v4 = Vec(D, {'a': 10, 'b': 10})
a = vec_select([v1, v2, v3, v4], 'a') 
assert a == [Vec(D,{'b': 1}), Vec(D,{'b': 2})]
    



def vec_sum(veclist, D): 
    '''
    >>> D = {'a','b','c'}
    >>> v1 = Vec(D, {'a': 1})
    >>> v2 = Vec(D, {'a': 0, 'b': 1})
    >>> v3 = Vec(D, {        'b': 2})
    >>> v4 = Vec(D, {'a': 10, 'b': 10})
    >>> vec_sum([v1, v2, v3, v4], D) == Vec(D, {'b': 13, 'a': 11})
    True
    '''
    v_sum=Vec(D,{d:0 for d in D})
    for v in veclist:
        v_sum += v
    return v_sum

D = {'a','b','c'}
v1 = Vec(D, {'a': 1})
v2 = Vec(D, {'a': 0, 'b': 1})
v3 = Vec(D, {        'b': 2})
v4 = Vec(D, {'a': 10, 'b': 10})
a = vec_sum([v1, v2, v3, v4], D) 
assert a == Vec(D, {'b': 13, 'a': 11})



def vec_select_sum(veclist, k, D): 
    '''
    >>> D = {'a','b','c'}
    >>> v1 = Vec(D, {'a': 1})
    >>> v2 = Vec(D, {'a': 0, 'b': 1})
    >>> v3 = Vec(D, {        'b': 2})
    >>> v4 = Vec(D, {'a': 10, 'b': 10})
    >>> vec_select_sum([v1, v2, v3, v4], 'a', D) == Vec(D, {'b': 3})
    True
    '''
    
    return vec_sum(vec_select(veclist, k), D)
D = {'a','b','c'}
v1 = Vec(D, {'a': 1})
v2 = Vec(D, {'a': 0, 'b': 1})
v3 = Vec(D, {        'b': 2})
v4 = Vec(D, {'a': 10, 'b': 10})
a = vec_select_sum([v1, v2, v3, v4], 'a', D)
assert a == Vec(D, {'b': 3})
 


## Problem 2
def scale_vecs(vecdict):
    '''
    >>> v1 = Vec({1,2,3}, {2: 9})
    >>> v2 = Vec({1,2,4}, {1: 1, 2: 2, 4: 8})
    >>> scale_vecs({3: v1, 5: v2}) == [Vec({1,2,3},{2: 3.0}), Vec({1,2,4},{1: 0.2, 2: 0.4, 4: 1.6})]
    True
    '''
    
    return [vecdict[k]/k for k in vecdict.keys() ]

v1 = Vec({1,2,3}, {2: 9})
v2 = Vec({1,2,4}, {1: 1, 2: 2, 4: 8})
a = scale_vecs({3: v1, 5: v2}) 
assert a == [Vec({1,2,3},{2: 3.0}), Vec({1,2,4},{1: 0.2, 2: 0.4, 4: 1.6})]

## Problem 3
def GF2_span(D, L):
    '''
    >>> from GF2 import one
    >>> D = {'a', 'b', 'c'}
    >>> L = [Vec(D, {'a': one, 'c': one}), Vec(D, {'b': one})]
    >>> len(GF2_span(D, L))
    4
    >>> Vec(D, {}) in GF2_span(D, L)
    True
    >>> Vec(D, {'b': one}) in GF2_span(D, L)
    True
    >>> Vec(D, {'a':one, 'c':one}) in GF2_span(D, L)
    True
    >>> Vec(D, {x:one for x in D}) in GF2_span(D, L)
    True
    '''
    from GF2 import one
    span=[]
    S=2**len(L)
    for i in range(S) :
        ms = [one if (len(bin(i))-2 >k and bin(i)[len(bin(i))-k-1]=='1') else 0 for k in reversed(range(len(L)))]
        v_sum=Vec(D,{})
        for j in range(len(L)):
            v_sum+=ms[j]*L[j]
        span.append(v_sum)
    
    return span

from GF2 import one
D = {'a', 'b', 'c'}
L = [Vec(D, {'a': one, 'c': one}), Vec(D, {'b': one})]
assert len(GF2_span(D, L))==4
assert Vec(D, {}) in GF2_span(D, L)
assert Vec(D, {'b': one}) in GF2_span(D, L)
assert Vec(D, {'a':one, 'c':one}) in GF2_span(D, L)
assert Vec(D, {x:one for x in D}) in GF2_span(D, L)

## Problem 4
# Answer with a boolean, please.

is_it_a_vector_space_1 = True
is_it_a_vector_space_2 = False



## Problem 5
is_it_a_vector_space_3 = True
is_it_a_vector_space_4 = False


## Problem 6

is_it_a_vector_space_5 = True
is_it_a_vector_space_6 = False
