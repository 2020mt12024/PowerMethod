import numpy as np

def PowerMethodDomEigVal(A,x,n,e):    
    xn = x
    q_prev = 0
    for i in range(n):        
        q = np.dot(xn.transpose(),np.dot(A,xn))/np.dot(xn.transpose(),xn)
        d = np.sqrt(np.dot(np.dot(A,xn).transpose(),np.dot(A,xn))/np.dot(xn.transpose(),xn) - q*q)
        xn = np.dot(A,xn)
        
        xn = xn/max(xn)
        print('{0: >20}'.format('Iteration: ') + str(i))
        print('{0: >20}'.format('Rayleigh Quotient: ')+str(q.max()))
        print('{0: >20}'.format('Error Bound: ')+str(d.max())+"\n")
        
        if(np.abs(q-q_prev) < e and i != 0):
            return   
        q_prev = q
M = np.array([[4,2,3],[2,7,6],[3,6,4]])
x_init = np.array([[1],[1],[1]])
print('A: ')
print(M)
print('x0: ')
print(x_init)
print("\nFinding Dominant Eigenvalues by Power Method (maxiteration="+str(10)+", tolerance="+str(0.000001)+"):\n")
PowerMethodDomEigVal(M,x_init,10,0.000001)