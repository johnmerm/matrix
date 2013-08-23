# version code 988
# Please fill out this stencil and submit using the provided submission script.

from matutil import *
from GF2 import one



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
    previous_row_pos = -1
    for r in A:
        c_pos = next((r.index(l) for l in r if l!=0 ),len(r))
        if previous_row_pos >=c_pos:
            return False
        previous_row_pos = c_pos
    return True
                 
def test_is_echelon():
    if is_echelon([[2,1,0],[0,-4,0],[0,0,1]]): print("OK 1")
    if not is_echelon([[2,1,0],[-4,0,0],[0,0,1]]): print("OK 2")
    if not is_echelon([[2,1,0],[0,3,0],[1,0,1]]): print("OK 3")
    if is_echelon([[1,1,1,1,1],[0,2,0,1,3],[0,0,0,5,3]]): print("OK 4")
    if is_echelon([[1,1,1,1,1],[0,2,0,1,3],[0,0,0,5,3],[0,0,0,0,0]]): print("OK 5")
    if not is_echelon([[1,1,1,1,1],[0,2,0,1,3],[0,0,0,5,3],[0,0,0,0,0],[0,0,0,0,1]]): print("OK 6")



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
    pass



## Problem 6
rowlist = [ ... ]    # Provide as a list of Vec instances
label_list = [ ... ] # Provide as a list
b = [ ... ]          # Provide as a list



## Problem 7
null_space_rows_a = {...} # Put the row numbers of M from the PDF



## Problem 8
null_space_rows_b = {...}



## Problem 9
# Write each vector as a list
closest_vector_1 = [...]
closest_vector_2 = [...]
closest_vector_3 = [...]



## Problem 10
# Write each vector as a list

project_onto_1 = [...]
projection_orthogonal_1 = [...]

project_onto_2 = [...]
projection_orthogonal_2 = [...]

project_onto_3 = [...]
projection_orthogonal_3 = [...]



## Problem 11
norm1 = ...
norm2 = ...
norm3 = ...
