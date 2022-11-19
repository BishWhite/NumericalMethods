import numpy as np
import matplotlib.pyplot as plt

dh = 1.00369

t1 = [0 for _ in range(10000)]
t2 = [0 for _ in range(10000)]
t3 = [0 for _ in range(10000)]
t4 = [0 for _ in range(10000)]
t5 = [0 for _ in range(10000)]
t6 = [0 for _ in range(10000)]
d1 = [0 for _ in range(10000)]


def D(h,f,x):
    return abs(f(h,x)-np.cos(x))


def f1(h,x):
    return (np.sin(x+h)-np.sin(x))/h

def f2(h,x):
    return (np.sin(x+h)-np.sin(x-h))/(2*h)

def f3(h,x):
    return (-np.sin(x+2*h)+8*np.sin(x+h)-8*np.sin(x-h)+np.sin(x-2*h))/(12*h)

def fill(x,y):
    d = pow(10,-16)
    for i in range(10000):
        t1[i] = D(d,f1,x)
        t2[i] = D(d,f2,x)
        t3[i] = D(d,f3,x)
        t4[i] = abs(f1(d,y))
        t5[i] = abs(f2(d,y))
        t6[i] = abs(f3(d,y))
        d1[i] = d
        d*=dh
    
    print(d)

fill(1,np.pi/2)

fig, axs = plt.subplots(3, 2, figsize=(6, 8),
                        constrained_layout=True)
ax = axs[0,0]
ax.plot(d1,t1, lw=0.15)
ax.set_yscale('log')
ax.set_xscale('log')
ax.set_xlim([10**(-16),1])
ax.set_ylim([10**(-16),1])
#ax.set_xticks([10**(-16)+0.001*i for i in range(1000)])

ax = axs[0,1]
ax.plot(d1,t2,lw=0.15)
ax.set_yscale('log')
ax.set_xscale('log')
ax.set_xlim([10**(-16),1])
ax.set_ylim([10**(-16),1])

ax = axs[1,0]
ax.plot(d1,t3,lw=0.15)
ax.set_yscale('log')
ax.set_xscale('log')
ax.set_xlim([10**(-16),1])
ax.set_ylim([10**(-16),1])

ax = axs[1,1]
ax.plot(d1,t4,lw=0.15)
ax.set_yscale('log')
ax.set_xscale('log')
ax.set_xlim([10**(-16),1])
ax.set_ylim([10**(-16),1])

ax = axs[2,0]
ax.plot(d1,t5,lw=0.1)
ax.set_yscale('log')
ax.set_xscale('log')
ax.set_xlim([10**(-16),1])
ax.set_ylim([10**(-16),1])

ax = axs[2,1]
ax.plot(d1,t6,lw=0.1)
ax.set_yscale('log')
ax.set_xscale('log')
ax.set_xlim([10**(-16),1])
ax.set_ylim([10**(-16),1])

plt.show()

plt.clf()



