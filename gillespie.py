import numpy as np
import matplotlib
matplotlib.use('tkagg')
import matplotlib.pyplot as plt
#import matplotlib.animation as animation
#from matplotlib.animation import FuncAnimation
import random


X = [20]
Y = [30]
t = [0]

tend = 1000

k1 = 50.0
k2 = 0.5
k3 = 5.0e-7
k4 = 0.05


A = 1
B = 3
#Bcrit = k1**2*k3*A**2/(k2*k4**2)+k4/k2
k2c=(k1*A/k4)**2*(k3/B)+k4/B
#k2=k2c
Bcrit = k1**2*k3*A**2/(k2*k4**2)+k4/k2
print(k2c)
print((k1/k4)*A , k2*k4*B/(k1*k3*A)) #pto fijo
#x0 = 10
#y0 = 20

i=0

while t[-1] < tend:

	
	current_X = X[-1]
	current_Y = Y[-1]

	rates = [k1*A, k2*current_X*Bcrit, k3*(current_X)*0.5*(current_X-1)*(current_Y), k4*current_X]
	suma = sum(rates)

	#tau = np.random.exponential(scale=1/suma)
	tau=-(1/suma)*np.log(random.random())

	t.append(t[-1] + tau)
	rand = random.uniform(0,1)

	# reaccion 1
	if rand*suma > 0 and rand*suma <= rates[0]:
		X.append(X[-1] + 1)
		Y.append(Y[-1])
	# reaccion 2
	elif rand*suma > rates[0] and rand*suma <= rates[0] + rates[1]:
		X.append(X[-1] - 1)
		Y.append(Y[-1] + 1)

	# reaccion 3
	elif rand*suma > rates[0]+rates[1] and rand*suma <= rates[0]+rates[1]+rates[2]:
		X.append(X[-1] + 1)
		Y.append(Y[-1] - 1)

	#reaccion 4
	elif rand*suma > rates[0]+rates[1]+rates[2] and rand*suma <= rates[0]+rates[1]+rates[2]+rates[3]:
		X.append(X[-1] - 1)
		Y.append(Y[-1])

	i += 1

print(t[-1], len(t))

fig, (ax1, ax2)=plt.subplots(1,2)
ax1.plot(t,X)
ax1.plot(t,Y)
ax1.set_xlabel("Tiempo")
ax1.set_ylabel("Concentración")
ax1.legend(["Especie U", "Especie V"])
ax1.set_title("Concentración vs tiempo")


ax2.plot(X,Y)
ax2.plot((k1/k4)*A , k2*k4*B/(k1*k3*A),'.r')
ax2.set_title("Espacio de fases")
plt.show()

#fig=plt.figure()
#ax = plt.axes(xlim=(0, np.amax(X)), ylim=(0, np.amax(Y)))
#line, = ax.plot([], [], lw=2)

# para animaciones, REQUIERE FFMPEG
#def init():
#    line.set_data([], [])
#    return line,
#
#def animate(i):
#    line.set_data(X[:500*i], Y[:500*i])
#    return line,
#
#plt.title(f"Espacio de fases")
#plt.xlabel("Concentración X")
#plt.ylabel("Concentración Y")
#
#
#writer = animation.FFMpegWriter(fps=30)
#anim = animation.FuncAnimation(fig, animate, frames=1000, #repeat=False, blit=True)
#anim.save("fases.mp4", writer=writer)

#

