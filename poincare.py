import matplotlib
import matplotlib.pyplot as plt
import numpy as np

plt.figure()

#parametros
a=1
b=4

#nulclinas
x=np.linspace(0.1,10,500)
y=np.linspace(0.1,10,500)

y1=-a/x**2+(b+1)/x
y2=b/x

#buscamos y pintamos el punto fijo (corte nulclinas)
fijox=a
fijoy=b/a


plt.plot(fijox, fijoy, '.r')
xm=np.linspace(0,10,15)
ym=np.linspace(0,10,15)
X, Y=np.meshgrid(xm,ym)


DX=a-(b+1)*X+X**2*Y
DY=b*X-X**2*Y
M=np.sqrt(DX**2+DY**2)


dirX=DX/M
dirY=DY/M



plt.xlim([0,10])
plt.ylim([0,10])
plt.plot(x, y1, color='blue')
plt.plot(x,y2, color='green')

plt.plot(fijox, fijoy, '.r')

plt.quiver(X , Y , dirX, dirY, width=0.004, pivot='mid') 


plt.show()
