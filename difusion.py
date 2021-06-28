import numpy as np
import matplotlib.pyplot as plt


#constantes
a=4.5
difx=0.001
dify=0.008
eta=np.sqrt(difx/dify)
#Supercriticality;
mu=0.98
bcrit=(1+a*eta)**2
b=bcrit*(mu+1)
 

size = 100  # size of the 2D grid
dx = 2.0 / size  # space step

T = 30.0  # total time
dt = 0.01  # time step
n = int(T / dt)  # number of iterations

U = np.array(np.random.rand(size, size), dtype='float64')  #Inicialization, random noise from 0 to 1.
V = np.array(np.random.rand(size, size), dtype='float64')

def laplacian(Z):
	Ztop = Z[0:-2, 1:-1]
	Zleft = Z[1:-1, 0:-2]
	Zbottom = Z[2:, 1:-1]
	Zright = Z[1:-1, 2:]
	Zcenter = Z[1:-1, 1:-1]
	return (Ztop + Zleft + Zbottom + Zright -
		4 * Zcenter) / dx**2

def show_patterns(U, ax=None):
	ax.imshow(U, cmap=plt.cm.cool, 
		interpolation='bilinear', 
		extent=[-1, 1, -1, 1])
	ax.set_axis_off()


#fig, axes = plt.subplots(3, 4, figsize=(8, 8))
#step_plot = n // 12
# We simulate the PDE with the finite difference
# method.
for i in range(n):
# We compute the Laplacian of u and v.
	deltaU = laplacian(U)
	deltaV = laplacian(V)
	#print(deltaU)
# We take the values of u and v inside the grid.
	Uc = U[1:-1, 1:-1]
	Vc = V[1:-1, 1:-1]
 
# We update the variables.
	U[1:-1, 1:-1], V[1:-1, 1:-1] = \
		Uc + dt * (difx * deltaU + a-(b+1)*Uc+Uc**2*Vc), \
		Vc + dt * (b * Uc-Uc**2*Vc+dify*deltaV)
# Neumann conditions: derivatives at the edges
# are null.
	for Z in (U, V):
		Z[0, :] = Z[1, :]
		Z[-1, :] = Z[-2, :]
		Z[:, 0] = Z[:, 1]
		Z[:, -1] = Z[:, -2]

# We plot the state of the system at
# 9 different times.
	#if i % step_plot == 0 and i < 12 * step_plot:
	#	ax = axes.flat[i // step_plot]
	#	show_patterns(U, ax=ax)
	#	ax.set_title(f'$t={i * dt:.2f}$')


fig, ax = plt.subplots(1, 1, figsize=(8, 8))
show_patterns(U, ax=ax)


plt.show()
