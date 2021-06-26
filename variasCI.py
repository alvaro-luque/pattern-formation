import numpy as np
import matplotlib.pyplot as plt 
from scipy.integrate import odeint

def modelo(v,t,p):
	[X, Y] = v
	[k1, k2, k3, k4, A, B] = p
	
	# vector de ecuaciones f=[x',y']
	f=[ k1*A-k2*B*X+k3*X**2*Y-k4*X , k2*B*X-k3*X**2*Y
	 ]
	
	return f

#pasamos los parametros
k1 = 50.000
k2 = 0.500
k3 = 5.0e-7
k4 = 0.05


A = 1	
B = k1**2*k3*A**2/(k2*k4**2)+k4/k2 #condición bcrit=a^2+1 con dimensiones
	
print(A,B)
print((k1/k4)*A , k2*k4*B/(k1*k3*A))
p=[k1,k2,k3,k4,A,B]	
t=np.linspace(0, 1000, 800)
plt.figure()
plt.title("Espacio de fases")
plt.xlabel("Concentración especie U")
plt.ylabel("Concentración especie V")
for x0,y0 in np.nditer([range(1000, 2000, 200),range(1000, 2000, 200)]):
	#for y0 in range(1000, 2000, 200):
	w0=[x0,y0]
	sol=odeint(modelo, w0, t, args=(p,))
	x=sol[:,0]
	y=sol[:,1]
	plt.plot(x,y, label="C.I. ({0}, {1})".format(w0[0], w0[1]))
#	print(w0[0], w0[1])

plt.legend()
plt.show()	
