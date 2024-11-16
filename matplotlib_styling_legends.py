import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,10,11)
print(x)

fig=plt.figure()
ax=fig.add_axes([0,0,1,1])
ax.plot(x,x)
ax.plot(x,x**2)
plt.show()

fig=plt.figure()
ax=fig.add_axes([0,0,1,1])
ax.plot(x,x,label='X vs X')
ax.plot(x,x**2,label='X vs X^2')
ax.legend()
plt.show()