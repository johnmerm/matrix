def getitem(v,d):
    "Returns the value of entry d in v"
    assert d in v.D
    return v.f[d] if d in v.f else 0

def setitem(v,d,val):
    "Set the element of v with label d to be val"
    assert d in v.D
    v.f[d]=val
    return v

def equal(u,v):
    "Returns true iff u is equal to v"
    assert u.D == v.D
    for i in u.D:
        if getitem(u, i) != getitem(v, i):
            return False
    return True
    

def add(u,v):
    "Returns the sum of the two vectors"
    assert u.D == v.D
    f={d:getitem(v, d)+getitem(u, d) for d in u.D if (d in v.f or d in u.f)}
    return Vec(v.D,f)
    

def dot(u,v):
    "Returns the dot product of the two vectors"
    assert u.D == v.D
    val=0
    for d in u.D:
        val+=(getitem(u, d)*getitem(v, d))
    return val

def scalar_mul(v, alpha):
    "Returns the scalar-vector product alpha times v"
    f={d:alpha*v.f[d] for d in v.f.keys()}
    return Vec(v.D,f)

def neg(v):
    "Returns the negation of a vector"
    f={d:-1*v.f[d] for d in v.f.keys()}
    return Vec(v.D,f)

##### NO NEED TO MODIFY BELOW HERE #####
class Vec:
    """
    A vector has two fields:
    D - the domain (a set)
    f - a dictionary mapping (some) domain elements to field elements
        elements of D not appearing in f are implicitly mapped to zero
    """
    def __init__(self, labels, function=None):
        if function == None:
            f = {x:y for (x,y) in list(enumerate(labels))}
            self.D=set(f.keys())
            self.f=f
        else:
            self.D = labels
            self.f = function

    __getitem__ = getitem
    __setitem__ = setitem
    __neg__ = neg
    __rmul__ = scalar_mul #if left arg of * is primitive, assume it's a scalar
    
    
       
        
    def __mul__(self,other):
        #If other is a vector, returns the dot product of self and other
        if isinstance(other, Vec):
            return dot(self,other)
        else:
            return NotImplemented  #  Will cause other.__rmul__(self) to be invoked

    def __truediv__(self,other):  # Scalar division
        return (1/other)*self

    __add__ = add

    def __radd__(self, other):
        "Hack to allow sum(...) to work with vectors"
        if other == 0:
            return self
    
    def __sub__(self,b):
         "Returns a vector which is the difference of a and b."
         return self+(-b)

    __eq__ = equal

    def __str__(self):
        "pretty-printing"
        try:
            D_list = sorted(self.D)
        except TypeError:
            D_list = sorted(self.D, key=hash)
        numdec = 3
        wd = dict([(k,(1+max(len(str(k)), len('{0:.{1}G}'.format(self[k], numdec))))) if isinstance(self[k], int) or isinstance(self[k], float) else (k,(1+max(len(str(k)), len(str(self[k]))))) for k in D_list])
        # w = 1+max([len(str(k)) for k in D_list]+[len('{0:.{1}G}'.format(value,numdec)) for value in self.f.values()])
        s1 = ''.join(['{0:>{1}}'.format(k,wd[k]) for k in D_list])
        s2 = ''.join(['{0:>{1}.{2}G}'.format(self[k],wd[k],numdec) if isinstance(self[k], int) or isinstance(self[k], float) else '{0:>{1}}'.format(self[k], wd[k]) for k in D_list])
        return "\n" + s1 + "\n" + '-'*sum(wd.values()) +"\n" + s2

    def __repr__(self):
        return "Vec(" + str(self.D) + "," + str(self.f) + ")"

    def copy(self):
        "Don't make a new copy of the domain D"
        return Vec(self.D, self.f.copy())
