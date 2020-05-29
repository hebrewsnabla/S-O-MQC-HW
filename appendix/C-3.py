import numpy as np
import copy
import sys

a = 3.00
b = 2.00
k = 1.000
k1 = 0.100
k2 = float(sys.argv[1])
A = 1
B = 0.5
v = 2

X = [np.array([3.3, 1.8]), 
     np.array([3.0, 1.5]),
     np.array([2.7, 2.1])]
X = np.array(X)
def bar(x):
    return np.mean(x, axis=0)

def getE(xy):
    x,y = xy[0], xy[1]
    return 0.5*k*(x-a)**2 + 0.5*k1*(y-b)**2 + k2*x*y 

E = np.zeros(3)
for i in [0,1,2]:
    E[i] = getE(X[i])
#Emin = E.min()
print(X,bar(X),E,E.min())

def update(X,E,h,Xs):
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

cyc = 1
while(True):
    oldX = copy.copy(X)
    oldE = copy.copy(E)
    #print(oldX, oldE)
    #h=0
    print("Cycle %d"%cyc)
    h, Emax = findh(E)
    #print(h, Emax)
    #while(h<3):
    Xs = (1+A)*bar(X) - A*X[h]
    Es = getE(Xs)
    if E.min() < Es < E[h]:
        X,E = update(X,E,h, Xs)
    elif Es < E.min():
        Xss = v*Xs + (1-v)*bar(X)
        Ess = getE(Xss)
        if Ess < E.min():
            X,E = update(X,E,h,Xss)
        else:
            X,E = update(X,E,h,Xs)
    else:
        Xss = B*X[h] + (1-B)*bar(X)
        Ess = getE(Xss)
        if Ess > E[h]:
            print("conv failed")
            break
        else:
            X,E = update(X,E,h,Xss)
    #h += 1
    #print(X,bar(X),E,E.min())
    print('bar(X):', bar(oldX), '->', bar(X))
    print('E     :', oldE, '->', E)
    dX = bar(X) - bar(oldX)
    if conv(dX):
        break
    else:
        cyc += 1

