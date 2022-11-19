import numpy as np

N = 23

stored_cos = np.array([0 for _ in range(N+1)], dtype="float64")
e = np.array([0 for _ in range (3*N+1)], dtype="float64")

def fill_e():
    e[0] = 1
    e[1] = 1/np.float64(np.exp(1))
    for i in range(2,e.size):
        e[i] = e[i-1]*e[1]


#Prove that cos(nx)=2cos((n−1)x)cos(x)−cos((n−2)x)
def fill_c(x):
    stored_cos[0] = 1
    stored_cos[1] = np.float64(np.cos(x))
    stored_cos[2] = np.float64(2*stored_cos[1]*stored_cos[1]) - 1

    for i in range(3,N+1):
        stored_cos[i] = np.float64(2*stored_cos[i-1]*stored_cos[1] - stored_cos[i-2])

def f(x):

    fill_e()
    fill_c(x*x*x*x)
    res = np.float64(1)
    for i in range(1,N+1):
        res += stored_cos[i]*e[i]*(e[3*i]-stored_cos[i])+e[i]
        
    return res

print(f(1))
