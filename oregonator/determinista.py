import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.optimize import fsolve 

#matplotlib.use("TkAgg")
def modelo(v,t,p):
	[X, Y, Z] = v
	[eps, delta, q, f] = p
	
	# vector de ecuaciones f=[x',y']
	g=[ (1/eps)*(X+q*Y-X**2-X*Y) , (1/delta)*(-q*Y+f*Z-X*Y) , X-Z
	 ]
	
	return g
	

#pasamos los parametros; CONSIDERAMOS SIEMPRE A=B=1 (paper)
eps=0.1
delta=0.4
q=0.0008
f = 0.72
p=[eps, delta, q, f]
#condiciones iniciales
X0=.1
Y0=.3
Z0=.1
w0=[X0,Y0, Z0]

#tiempo
t=np.linspace(0, 1000, 1500)
sol=odeint(modelo, w0, t, args=(p,))
x=sol[:,0]
y=sol[:,1]
z=sol[:,2]

#resolvemos el punto fijo
def cositas(z):
	u=z[0]
	v=z[1]
	w=z[2]
	
	F=np.empty(3)
	F[0]=u+q*v-u**2-u*v
	F[1]=-q*v+f*w-u*v
	F[2]=u-w
	return F

zGuess=np.array([1,1,1])
fijo=fsolve(cositas, zGuess)
print(fijo)
#gráficas

'''
fig1, (ax1, ax2) = plt.subplots(1,2)
ax1.set_title("Concentración vs tiempo")
ax1.set_xlabel("Tiempo")
ax1.set_ylabel("Concentración")
ax1.plot(t,x)
ax1.plot(t,y)
ax1.plot(t,z)
ax1.legend(["Especie U", "Especie V", "Especie W"])

ax2.set_xlabel("Concentración especie U")
ax2.set_ylabel("Concentración especie V")
ax2.set_title("Proyección UV")
ax2.plot(x,y)
#ax2.plot((k1/k4)*A , k2*k4*B/(k1*k3*A),'.r')

fig2, (ax3, ax4) = plt.subplots(1,2)
ax3.set_xlabel("Concentración especie U")
ax3.set_ylabel("Concentración especie W")
ax3.set_title("Proyección UW")
ax3.plot(x,z)

ax4.set_xlabel("Concentración especie V")
ax4.set_ylabel("Concentración especie W")
ax4.set_title("Proyección VW")
ax4.plot(y,z)
'''

plt.figure(1)
plt.title("Concentración vs tiempo")
plt.xlabel("Tiempo")
plt.ylabel("Concentración")
plt.plot(t,x)
plt.plot(t,y)
plt.plot(t,z)
plt.legend(["Especie U", "Especie V", "Especie W"])

fig2 = plt.figure(2)
ax = fig2.gca(projection="3d")
ax.plot(x,y,z)
ax.set_title("Espacio de fases, f={0}".format(f))
ax.set_xlabel("Concentración U")
ax.set_ylabel("Concentración V")
ax.set_zlabel("Concentración W")
ax.plot(fijo[0], fijo[1], fijo[2], '.r')
plt.show()
