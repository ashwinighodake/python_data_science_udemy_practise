import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,10,11)
fig=plt.figure()
ax=fig.add_axes([0.1,0.1,0.8,0.8])
ax.plot(x,x,color='purple')
plt.show()

fig=plt.figure()
ax=fig.add_axes([0.1,0.1,0.8,0.8])
ax.plot(x,x,color='#e6c017',label='X vs X')
ax.plot(x,x+1,color='purple',label='X vs X+1')
ax.legend()
plt.show()

fig=plt.figure()
ax=fig.add_axes([0.1,0.1,0.8,0.8])
ax.plot(x,x,color='#e6c017',label='X vs X',lw=1,ls='--')
lines=ax.plot(x,x+1,color='purple',label='X vs X+1',lw=1,ls='-.')
ax.plot(x,x+5,color='purple',lw=2,marker='+',markersize=20)
ax.plot(x,x+3,color='purple',lw=2,marker='o',ls='--',ms=10,markerfacecolor='red',markeredgewidth=4,markeredgecolor='orange')
lines[0].set_dashes([1,1,1,2,3,5])
ax.legend()
plt.show()