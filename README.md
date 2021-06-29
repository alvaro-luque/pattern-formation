# pattern-formation
This repository contains several python code files for simulating the Belousov-Zhabotinsky reaction-diffusion system in both the Brusselator and Oregonator historical approaches. Some code uses deterministic algorithms to solve the PDEs of the system numerically whilst the file gillespie.py contains a stochastic approach to the problem.

As the title says, the main goal of the project is to simulate Turing patterns in an oscillating chemical reaction. Turing patterns arise when a certain instability condition is met; in this case, we focus on diffusion-driven instabilities. A thorough linear stability analysis provides us with the necessary conditions on the diffusion parameters of the problem to create static patterns arising from random noise initial states, for example:

![patron098](https://user-images.githubusercontent.com/86519267/123764712-5455d400-d8c5-11eb-95f4-c8f9490c16c4.png)

Another interesting feature of the project is the difference between the deterministic and stochastic approaches, which both yield coherent results with the experiment, each of them having very different nature. The Gillespie stochastic simulation algorithm (GSSA) provides a unique solution to the master equation of the problem. The main characteristic of the algorithm is the random sampling of the time step used in each iteration. In the context of the problem, another random number is generated to "decide" which reaction is going to take place, which surprisingly reproduces the results according to other techniques and previous work on the subject. The next figures are presented as a comparison of the results obtained between both methods. We can see the temporal profile of the concentration of two chemicals (oscillating as predicted) and the phase space of the system, showing again the characteristic oscillatory behaviour. First we have a look at the deterministic solution


![determinista_inestable](https://user-images.githubusercontent.com/86519267/123767324-a861b800-d8c7-11eb-904a-dfeef8656446.png)

This solution and the solution provided by GSSA are quite similar:

![gillespiefijo](https://user-images.githubusercontent.com/86519267/123766370-ee6a4c00-d8c6-11eb-9660-994c7ec513c0.png)

Many other features of the system can be simulated with the provided files, such as limit cycle or stable fixed point behaviour, as well as plotting the vectorial field associated to the time evolution of the chemicals to apply the [Poincaré-Bendixson theorem](http://www.cds.caltech.edu/archive/help/uploads/wiki/files/179/lecture5Bs.pdf).

Please note that these files were created for a university project, therefore this repository is intended for our teachers to check our work. The files are somewhat messy and many commented sections fulfill the purpose of being practical for quick simulations from which we want to obtain different results.
