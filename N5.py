from collections import deque
import matplotlib.pyplot as plt

N = 1001

xn = [(n - 1) / (N - 1) for n in range(1, N)]

y = [1]

for i in range(1, N - 2):
    y.append(y[i-1]/(1/1000000+2))

y.append(1)

u = deque([y[N - 2]])

for i in range(N - 3, 0, -1):
    u.appendleft((y[i] + u[0]) / ((1/1000000)+2))


u.appendleft(1)

plt.plot(xn, u, lw=.5)
plt.ylabel("U")
plt.xlabel("Xn")

plt.show()

print(u)
