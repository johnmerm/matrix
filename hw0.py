# Please fill out this stencil and submit using the provided submission script.

## Problem 1
def myFilter(L, num): return [ a for a in L if a%num !=0] 



## Problem 2
def myLists(L): return [ [1+b for b in range(a)] for a in L]



## Problem 3
def myFunctionComposition(f, g): return {a:g[f[a]] for a in f.keys() if f[a] in g}


## Problem 4
# Please only enter your numerical solution.

complex_addition_a = 5+3j 
complex_addition_b = 1j
complex_addition_c = (-1 + 0.001j)
complex_addition_d = 0.001 + 9j



## Problem 5
GF2_sum_1 = 1
GF2_sum_2 = 0
GF2_sum_3 = 0


## Problem 6
def mySum(L): 
    current = 0
    for x in L:
        current+=x
    return current



## Problem 7
def myProduct(L): 
    current = 1
    for x in L:
        current *=x
    return current


## Problem 8
def myMin(L): 
    current  = None
    for x in L:
        current = min(current,x) if (current!=None) else x
    return current



## Problem 9
def myConcat(L): 
    current = ""
    for x in L:
        current = current+""+x
    return current



## Problem 10
def myUnion(L): 
    current = set()
    for x in L:
        current.update(x)
    return current

