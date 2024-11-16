import numpy as np
import matplotlib.pyplot as plt

x=np.arange(0,10)
print(x)

y=2*x
print(y)
plt.plot(x,y)
plt.title('String Title')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
#plt.xlim(0,6)
#plt.ylim(0.15)
plt.show()
plt.savefig('myfirstplot.png')