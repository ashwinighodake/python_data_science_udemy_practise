import numpy as np
import matplotlib.pyplot as plt
a=np.linspace(0,10,11)
b=a**4

print(a)
print(b)

x=np.arange(0,10)
y=2*x

fig,axes=plt.subplots()
axes.plot(x,y)
plt.show()


fig,axes=plt.subplots(nrows=1,ncols=2)
axes[0].plot(x,y)
axes[1].plot(a,b)
fig.subplots_adjust(wspace=0.9)
plt.show()

fig,axes=plt.subplots(nrows=2,ncols=2)
axes[0][0].plot(x,y)
axes[0][1].plot(a,b)
axes[1][0].plot(x,y)
axes[1][1].plot(a,b)
fig.subplots_adjust(wspace=0.9)
plt.show()