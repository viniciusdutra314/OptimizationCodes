import matplotlib.pyplot as plt
import numpy as np
x_range=np.linspace(-5,5,1000)
y_range=np.linspace(-5,5,1000) 
X,Y=np.meshgrid(x_range,y_range)
func1=lambda x,y: np.exp(y) +x**2 -5*x
func2=lambda x,y: x**2 -y -y**2
func_interseccao=lambda x,y: func1(x,y)**2 + func2(x,y)**2
Z1=func1(X,Y)
Z2=func2(X,Y)
Z3=func_interseccao(X,Y)
plt.contour(X,Y,Z1,levels=[0],colors='r')
plt.contour(X,Y,Z2,levels=[0],colors='g')
plt.contour(X,Y,Z3,colors='y')
plt.grid(True)
plt.show()