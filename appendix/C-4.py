import numpy as np
import copy
import sys

a = 3.00
b = 2.00
k = 1.000
k1 = 0.100
k2 = 0.03 #float(sys.argv[1])
#A = 1
#B = 0.5
#v = 2

'''X = [np.array([3.3, 1.8]), 
     np.array([3.0, 1.5]),
     np.array([2.7, 2.1])]
X = np.array(X)'''
X = np.array([3.3, 1.8])
#def bar(x):
#    return np.mean(x, axis=0)

def getE(xy):
    x,y = xy[0], xy[1]
    return 0.5*k*(x-a)**2 + 0.5*k1*(y-b)**2 + k2*x*y 

def getf(xy):
    x,y = xy[0], xy[1]
    f = [k*(x-a) + k2*y, k1*(y-b) + k2*x]
    return np.array(f)
#E = np.zeros(3)
#for i in [0,1,2]:
E = getE(X)
#Emin = E.min()
#print(X,E)

'''def update(X,E,h,Xs):
    print("update %f,%f -> %f,%f"%(X[h][0],X[h][1],Xs[0],Xs[1]))
    X[h] = Xs
    newX = X
    E[h] = getE(Xs)
    newE = E
    return newX, newE

def findh(E):
    Emax = -100.0
    h = -1
    for i in range(len(E)):
        if E[i] > Emax:
            h = i
            Emax = E[i]
    return h, Emax
def conv(dx):
    thresh = 0.002
    cv = abs(dx[0]) < thresh and abs(dx[1]) < thresh
    return cv
'''
f = getf(X)
print("Cycle 0\n X: %f,%f  E: %f  f: %f,%f "%(X[0], X[1], E, f[0], f[1]))
oldE = E
oldX = copy.copy(X)
oldf = copy.copy(f)
oldalpha = 0.5
oldG = np.identity(2)
while(True):
    q = -oldalpha*oldf
    X = oldX + q
    E = getE(X)
    f = getf(X)
    if E > oldE:
        print("reset alpha")
        oldalpha /= 2
    else:
        print("Cycle 1\n X: %f,%f  E: %f  f: %f,%f"%(X[0], X[1], E, f[0], f[1]))
        print("Start Forming U")
        U = -1*np.dot(oldG, f + oldf*(oldalpha-1))
        d = f - oldf
        print("U: ", U, "d:", d)
        aa = 1.0/np.dot(U.T, d)
        T = np.dot(U.T, U) 
        print("a: %f  T: %f"%(aa,T), "aUf: %f"%((1/aa)*np.dot(U,oldf)))
        if (1/aa < 1e-5*T) or (abs((1/aa)*np.dot(U.T,oldf)) > 1e-5):
        #if False:
            print("reset G")
            G = np.identity(2)
            alpha = 0.5
        else:
            G = oldG + aa*np.einsum('i,j->ij', U, U)
            alpha = 1
        break
cyc = 2
while(True):
    oldX = copy.copy(X)
    oldE = E
    oldalpha = alpha
    oldG = copy.copy(G)
    oldf = copy.copy(f)
    #print(oldX, oldE)
    q = -oldalpha*np.dot(oldG, oldf)
    X = oldX + q
    E = getE(X)
    f = getf(X)
    print("Cycle %d\n X: %f,%f  E: %f  f: %f,%f"%(cyc, X[0], X[1], E, f[0], f[1]))
    U = -1*np.dot(oldG, f + oldf*(oldalpha-1))
    d = f - oldf
    print(U, d)
    aa = 1.0/np.dot(U.T, d)
    T = np.dot(U.T, U) 
    print("a: %f  T: %.9f"%(aa,T), "aUf: %.9f"% ((1/aa)*np.dot(U,oldf)))
    if (abs(aa*T > 1e5)) or (abs((1/aa)*np.dot(U.T,oldf)) > 1e-5):
    #if False:
        print("reset G")
        #break
        G = np.identity(2)
        alpha = 0.5
    else:
        G = oldG + aa*np.einsum('i,j->ij',U, U)
        alpha = 1

    if np.dot(f.T, f) < 1e-5:
        break
    else:
        cyc += 1
    if cyc > 30:
        print("conv not met")
        break
'''
'''