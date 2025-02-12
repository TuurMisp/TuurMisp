import numpy as np
import matplotlib.pyplot as plt

x = []
i = 0
#j = x1
j = 1
#k =
k = 0
x.append(j)
x.append(k)
residuals = []
iteraties = []
while abs(x[-1]-x[-2]) > 0.00001:
    i += 1
    j = 3*i+5/(1-2*i)
    x.append(j)
    residuals.append(abs(x[-1]-x[-2]))
    iteraties.append(i)
    plt.scatter(i,j, color = "r")
plt.show()
plt.yscale("log")
plt.scatter(iteraties,residuals, color = "g", label = "residuals")
plt.legend()
plt.show()