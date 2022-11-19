from collections import deque
import matplotlib.pyplot as plt

N = 1000
Fn = []

xk = [-1+2*k/N for k in range(N+1)]


def fill_fn(N):
    f = [1/26, 1/(1+25*xk[1]*xk[1])]
    for i in range(0, N-1):
        f.append(1/(1+25*xk[i+2]*xk[i+2]))
        Fn.append((f[i]-2*f[i+1]+f[i+2])*6*N*N/4)


fill_fn(N)

y = [Fn[0]/3]
y1 = [1/3]

for i in range(1, N-2):
    y.append((Fn[i] - y[i-1])/4)
    y1.append(-y1[i-1]/4)

y.append((Fn[N-2] - y[N-3])/3)
y1.append((1-y1[N-3])/3)

z = deque([y[N-2]/3])
q = deque([y1[N-2]/3])

for i in range(N-3, 0, -1):
    z.appendleft((y[i]-z[0])/4)
    q.appendleft((y1[i]-q[0])/4)

z.appendleft((y[0]-z[0])/3)
q.appendleft((y1[0]-q[0])/3)

w = []

for i in range(N-1):
    m = (z[0]+z[N-2])/(1+q[0]+q[N-2])
    w.append(z[i] - m*q[i])


plt.plot(xk[0:999], w, lw=.5)
plt.ylabel("W")
plt.xlabel("Xk")
plt.show()
