from math import sqrt
N=8
k=1
for N in [2**n for n in range (4,8)]:
    print("N="+str(N))
    
    x0 = 1/sqrt(N)
    x1 = 1/sqrt(N)

    for m in range(20):
        print( x1**2 )
        M = ((N-k)*x0-k*x1)/N
        x0 = (2*M - x0)
        x1 = (2*M + x1)
    


