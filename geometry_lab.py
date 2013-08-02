from mat import Mat
from math import *

## Task 1
def identity(labels = {'x','y','u'}):
    '''
    In case you have never seen this notation for a parameter before,
    the way it works is that identity() now defaults to having labels 
    equal to {'x','y','u'}.  So you should write your procedure as if 
    it were defined 'def identity(labels):'.  However, if you want the labels of 
    your identity matrix to be {'x','y','u'}, you can just call 
    identity().  Additionally, if you want {'r','g','b'}, or another set, to be the
    labels of your matrix, you can call identity({'r','g','b'}).  
    '''
    return Mat((labels,labels),{(x,y):1 for x in labels for y in labels if x == y})
## Task 2
def translation(x,y):
    '''
    Input:  An x and y value by which to translate an image.
    Output:  Corresponding 3x3 translation matrix.
    '''
    mat=  identity()
    
    mat['x','u'] = x
    mat['y','u'] = y
    
    return mat
    

## Task 3
def scale(a, b):
    '''
    Input:  Scaling parameters for the x and y direction.
    Output:  Corresponding 3x3 scaling matrix.
    '''
    mat=identity()
    
    mat['x','x'] = a
    mat['y','y'] = b
    
    return mat

## Task 4
def rotation(angle):
    '''
    Input:  An angle in radians to rotate an image.
    Output:  Corresponding 3x3 rotation matrix.
    Note that the math module is imported.
    '''
    mat=identity()
    
    mat['x','x'] = cos(angle)
    mat['y','y'] = cos(angle)
    
    mat['x','y'] = -sin(angle)
    mat['y','x'] = sin(angle)
    
    return mat

## Task 5
def rotate_about(x,y,angle):
    '''
    Input:  An x and y coordinate to rotate about, and an angle
    in radians to rotate about.
    Output:  Corresponding 3x3 rotation matrix.
    It might be helpful to use procedures you already wrote.
    '''
    return translation (x,y)* ( rotation(angle) * translation (-x,-y)) 


print(rotate_about(1,2,pi/4))
## Task 6
def reflect_y():
    '''
    Input:  None.
    Output:  3x3 Y-reflection matrix.
    '''
    mat = identity()
    mat['x','x'] = -1
    
    return mat

## Task 7
def reflect_x():
    '''
    Inpute:  None.
    Output:  3x3 X-reflection matrix.
    '''
    mat = identity()
    mat['y','y'] = -1
    
    return mat
    
## Task 8    
def scale_color(scale_r,scale_g,scale_b):
    '''
    Input:  3 scaling parameters for the colors of the image.
    Output:  Corresponding 3x3 color scaling matrix.
    '''
    mat  = identity({'r','g','b'})
    mat['r','r'] = scale_r
    mat['g','g'] = scale_g
    mat['b','b'] = scale_b

## Task 9
def grayscale():
    '''
    Input: None
    Output: 3x3 greyscale matrix.
    '''
    mat  = identity({'r','g','b'})
    v = {'r':77,'g':151,'b':28}
    
    for c1 in v.keys():
        for c2 in v.keys():
            mat[c1,c2] = v[c1]
    return mat / 256

## Task 10
def reflect_about(p1,p2):
    '''
    Input: 2 points that define a line to reflect about.
    Output:  Corresponding 3x3 reflect about matrix.
    '''
    mat = identity()
    mat['x','x'] = p1**2 - p2**2
    mat['x','y'] = 2*p1*p2
    mat['y','x'] = 2*p1*p2
    mat['y','y'] = p2**2 - p1**2
    
    mat = (1/(p1**2 + p2**2))*mat
    
    return mat
