import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#matplotlib.use("TkAgg")
def modelo(v,t,p):
	[X, Y] = v
	[k1, k2, k3, k4, A, B] = p
	
	# PDE vector f=[x',y'], see scipy.integrate documentation for more info on odeint.
	f=[ k1*A-k2*B*X+k3*X**2*Y-k4*X , k2*B*X-k3*X**2*Y
	 ]
	
	return f
	

#pasamos los parametros
k1 = 50.000
k2 = 0.500
k3 = 5.0e-7
k4 = 0.05


A = 1	
B = 1.7
Bcrit = k1**2*k3*A**2/(k2*k4**2)+k4/k2 #critical condition
#B=Bcrit #uncomment for limit cycle simulations
#a=(k1*np.sqrt(k3)*A)/(k4*np.sqrt(k4))
#b=k2*B/k4
print("Parameters A,B, Bcrit: {0}, {1}, {2}".format( A,B,Bcrit))
print("Fixed point: ({0},{1}) ".format( (k1/k4)*A , k2*k4*B/(k1*k3*A)))
p=[k1,k2,k3,k4,A,B]
#Initial conditions
X0=1000
Y0=1600
print("Initial conditions ({0},{1})".format(X0,Y0))
x0=X0*np.sqrt(k3/k4)
y0=Y0*np.sqrt(k3/k4)
w0=[X0,Y0]

#tiempo
t=np.linspace(0, 1000, 750)
sol=odeint(modelo, w0, t, args=(p,))
x=sol[:,0]
y=sol[:,1]

fig, (ax1, ax2) = plt.subplots(1,2)
ax1.set_title("Concentración vs tiempo")
ax1.set_xlabel("Tiempo")
ax1.set_ylabel("Concentración")
ax1.plot(t,x)
ax1.plot(t,y)
ax1.legend(["Especie U", "Especie V"])

ax2.set_xlabel("Concentración especie U")
ax2.set_ylabel("Concentración especie V")
ax2.set_title("Espacio de fases")
ax2.plot(x,y)
ax2.plot((k1/k4)*A , k2*k4*B/(k1*k3*A),'.r')

plt.show()
