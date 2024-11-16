import numpy as np
import matplotlib.pyplot as plt

a=np.linspace(0,10,11)
b=a**4
print(a)
print(b)

x=np.arange(0,10)
print(x)
y=2*x
print(y)

fig=plt.figure(figsize=(10,5))
axes=fig.add_axes([0.1,0.1,0.8,0.8])
axes.set_xlabel('x-axis')
axes.set_ylabel('y-axis')
axes.set_title('Power of 2')
axes.plot(x,y)
plt.show()


fig=plt.figure(figsize=(10,5))
axes=fig.add_axes([0.1,0.1,0.8,0.8])
axes.set_xlabel('x-axis')
axes.set_ylabel('y-axis')
axes.set_title('Power of 4')
axes.plot(a,b)
plt.show()

fig=plt.figure(figsize=(10,5))
axes1=fig.add_axes([0.1,0.1,0.8,0.8])
axes2=fig.add_axes([0.2,0.3,0.4,0.5])
axes1.set_xlabel('x-axis')
axes1.set_ylabel('y-axis')
axes1.set_title('Power of 2')
axes2.set_xlabel('x-log')
axes2.set_ylabel('y-log')
axes2.set_title('Power of 4')
axes1.plot(x,y)
axes2.plot(a,b)
plt.show()
fig.savefig('new_image.png',bbox_inches='tight')