# version code 988
# Please fill out this stencil and submit using the provided submission script.

from matutil import *
from GF2 import one
from vecutil import zero_vec,list2vec



## Problem 1
# Write each matrix as a list of row lists

echelon_form_1 = [[   1,2,0,2,0   ],
                  [   0,1,0,3,4   ],
                  [   0,0,2,3,4   ],
                  [   0,0,0,2,0   ],
                  [   0,0,0,0,4   ]]

echelon_form_2 = [[   0,4,3,4,4   ],
                  [   0,0,4,2,0   ],
                  [   0,0,0,0,1   ],
                  [   0,0,0,0,0   ]]

echelon_form_3 = [[   1,0,0,1   ],
                  [   0,0,0,1   ],
                  [   0,0,0,0   ]]

echelon_form_4 = [[   1,0,0,0   ],
                  [   0,1,0,0   ],
                  [   0,0,0,0   ],
                  [   0,0,0,0   ]]



## Problem 2
def is_echelon(A):
    '''
    Input:
        - A: a list of row lists
    Output:
        - True if A is in echelon form
        - False otherwise
    Examples:
        >>> is_echelon([[1,1,1],[0,1,1],[0,0,1]])
        True
        >>> is_echelon([[0,1,1],[0,1,0],[0,0,1]])
        False
    '''
    previous_row_pos = 2**64
    for r in reversed(A):
        c_pos = next((r.index(l) for l in r if l!=0 ),2**64)
        if c_pos == 2**64 and previous_row_pos == 2**64:
            continue
        if previous_row_pos <=c_pos:
            return False
        previous_row_pos = c_pos
    return True

# M1 = [[0,0,0],[0,0,0],[0,0,0]]
# M2 = [[1,0,0],[0,1,0],[0,1,0]]
# M3 = [[0]*4,[1]*4]
# M4 = [[1,0,0,0,0,0,0,0], [0,1,1,1,1,1,1,1],[0,0,1,1,1,0,1,0],[0,0,0,0,0,1,1,0]]
# M5 = [[1]]
# M6 = [[0]]                 
# 
# for M in [M1,M2,M3,M4,M5,M6]:
#     print(is_echelon(M))
#     print(listlist2mat(M))


## Problem 3
# Give each answer as a list

echelon_form_vec_a = [1,0,3,0]
echelon_form_vec_b = [-3,0,-2,3]
echelon_form_vec_c = [-5,0,2,0,2]



## Problem 4
# If a solution exists, give it as a list vector.
# If no solution exists, provide "None".

solving_with_echelon_form_a = None
solving_with_echelon_form_b = [21,0,2,0,0]



## Problem 5
def echelon_solve(rowlist, label_list, b):
    '''
    Input:
        - rowlist: a list of Vecs
        - label_list: a list of labels establishing an order on the domain of
                      Vecs in rowlist
        - b: a vector (represented as a list)
    Output:
        - Vec x such that rowlist * x is b
    >>> D = {'A','B','C','D','E'}
    >>> U_rows = [Vec(D, {'A':one, 'E':one}), Vec(D, {'B':one, 'E':one}), Vec(D,{'C':one})] 
    >>> b_list = [one,0,one]>>> cols = ['A', 'B', 'C', 'D', 'E']
    >>> echelon_solve(U_rows, cols, b_list)
    Vec({'B', 'C', 'A', 'D', 'E'},{'B': 0, 'C': one, 'A': one})
    '''
    x=zero_vec(set(label_list))
    for i in reversed(range(len(rowlist))):
        row = rowlist[i]
        j = next((l for l in label_list if row[l]!=0 ),None) # first non-zero element of row
        if j==None:
            continue
        
        res = row*x
        x[j] = (b[i] - res) / row[j]
    return x

cols = ['A', 'B', 'C', 'D', 'E']
D = set(cols)

U_rows = [Vec(D,{'E': one, 'D': one, 'A': 0, 'C': 0, 'B': one}), Vec(D,{'E': 0, 'D': one, 'A': 0, 'C': 0, 'B': 0}), Vec(D,{'E': 0, 'D': 0, 'A': one, 'C': one, 'B': 0}), Vec(D,{'E': 0, 'D': 0, 'A': 0, 'C': 0, 'B': 0})]
b_list = [0, 0, one, 0]
u = echelon_solve(U_rows, cols, b_list)
print([u_row*u for u_row in U_rows])
print(b_list)

U_rows=[Vec(D,{'E': one, 'D': one, 'A': one, 'C': one, 'B': one}), Vec(D,{'E': one, 'D': 0, 'A': 0, 'C': 0, 'B': one}), Vec(D,{'E': one, 'D': 0, 'A': 0, 'C': one, 'B': 0}), Vec(D,{'E': one, 'D': one, 'A': 0, 'C': 0, 'B': 0})]
b_list = [0, one, 0, one]
u=echelon_solve(U_rows, cols, b_list)
print([u_row*u for u_row in U_rows])
print(b_list)

U_rows = [Vec(D, {'A':one, 'C':one}), Vec(D, {'C':one, 'E':one}), Vec(D,{'D':one})]
b_list = [one, one, one]
u = echelon_solve(U_rows, cols, b_list)
print([u_row*u for u_row in U_rows])
print(b_list)


## Problem 6
D = {'A','B','C','D'}
rowlist = [ Vec(D, {'A':one,'B':one,        'D':one }),
            Vec(D, {        'B':one                 }),
            Vec(D, {                'C':one         }),
            Vec(D, {                        'D':one })]    # Provide as a list of Vec instances
label_list = ['A','B','C','D'] # Provide as a list

M=listlist2mat([[one,0,0,0],[one,one,0,0],[one,0,one,0],[one,0,one,one]])
g = [ one,0,one,0 ]          # Provide as a list
b = [one,one,0,0]            #b= M*list2vec(g)



## Problem 7
null_space_rows_a = {3,4} # Put the row numbers of M from the PDF



## Problem 8
null_space_rows_b = {4}

def project_along(b, a):
    sigma = (b*a)/(a*a) if a*a != 0 else 0
    return sigma * a

def project(b, a): 
    b=  list2vec(b)
    a= list2vec(a)
    sa = project_along(b, a)
    return (sa,b - sa )


## Problem 9
# Write each vector as a list
closest_vector_1 = [8/5,16/5]
closest_vector_2 = [0,1,0]
closest_vector_3 = [3,2,1,-4]



## Problem 10
# Write each vector as a list

project_onto_1 = [2,0]
projection_orthogonal_1 = [0,1]

project_onto_2 = [-1/6,-1/3,1/6]
projection_orthogonal_2 = [7/6,4/3,23/6]

project_onto_3 = [1,1,4]
projection_orthogonal_3 = [0,0,0]



## Problem 11
norm1 = 3
norm2 = 4
norm3 = 1

