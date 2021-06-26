import numpy as np
import matplotlib.pyplot as plt


#constantes
q=0.002
f=0.73
eps=1
#delta=4
difx=1
dify=75
#difz=.1

#eta=np.sqrt(difx/dify)
 

size = 150  # size of the 2D grid
#dx = 20.0 / size  # space step

T = 25.0  # total time
dt = 0.002  # time step
n = int(T / dt)  # number of iterations

#inicialización, ruido aleatorio entre 0 y 1
#U = np.zeros((size, size), dtype='float64')  
#V = np.zeros((size, size), dtype='float64')
U = np.array(np.random.rand(size,size), dtype='float64')
V = np.array(np.random.rand(size,size), dtype='float64')



#for j in range(1,4):
#	U[70,50-j]=U[70,50+j]=U[70+j,50]=U[70-j,50]=1
	
#for i in range(30,70):
#	U[i,50]=1
#W = np.array(np.random.rand(size, size), dtype='float64')

def laplacian(Z):
	Ztop = Z[0:-2, 1:-1]
	Zleft = Z[1:-1, 0:-2]
	Zbottom = Z[2:, 1:-1]
	Zright = Z[1:-1, 2:]
	Zcenter = Z[1:-1, 1:-1]
	return (Ztop + Zbottom + Zright + Zleft -
		4 * Zcenter)

def show_patterns(U, ax=None):
	ax.imshow(U, cmap=plt.cm.cool, 
		interpolation='bilinear', 
		extent=[-1, 1, -1, 1])
	ax.set_axis_off()


#fig, axes = plt.subplots(2, 3, figsize=(8, 8))
#plt.suptitle("Parámetros: f={0}, ε={1}".format(f, eps))
#step_plot = n // 10
# We simulate the PDE with the finite difference
# method.
for i in range(n):
# We compute the Laplacian of u and v.
	deltaU = laplacian(U)
	deltaV = laplacian(V)
	#deltaW = laplacian(W)
	#print(deltaU)
# We take the values of u and v inside the grid.
	Uc = U[1:-1, 1:-1]
	Vc = V[1:-1, 1:-1]
	#Wc = W[1:-1, 1:-1]
 
# We update the variables.
	U[1:-1, 1:-1], V[1:-1, 1:-1] = \
		Uc + dt * (difx * deltaU + (1/eps)*(Uc - Uc**2 -f*Vc*(Uc-q)/(Uc+q))), \
		Vc + dt * ((Uc-Vc)+dify*deltaV) \
# CONDICIONES PERIÓDICAS
	for Z in (U, V):
		Z[0, :] = Z[1, :]
		Z[-1, :] = Z[-2, :]
		Z[:, 0] = Z[:, 1]
		Z[:, -1] = Z[:, -2]

# We plot the state of the system at
# 9 different times.
	#if i % step_plot == 0 and i < 6 * step_plot:
	#	ax = axes.flat[i // step_plot]
	#	show_patterns(U, ax=ax)
	#	ax.set_title(f'$t={i * dt:.2f}$')


fig, ax = plt.subplots(1, 1, figsize=(8, 8))
show_patterns(U, ax=ax)


plt.show()
