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
y = [Fn[0]/4]

for i in range(1, N-1):
    y.append((Fn[i] - y[i-1])/4)

u = deque([y[N-2]/4])

for i in range(N-3, -1, -1):
    u.appendleft((y[i]-u[0])/4)

plt.plot(xk[0:999], u, lw=.5)
plt.ylabel("U")
plt.xlabel("Xk")
plt.show()



