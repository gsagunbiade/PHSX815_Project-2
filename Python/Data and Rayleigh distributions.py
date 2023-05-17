# -*- coding: utf-8 -*-
"""
Created on Mon May 15 14:56:06 2023

@author: g361a609
"""

import numpy as np
import matplotlib.pyplot as plt
import Random as rng

seed = 4445
random = rng.Random(seed)
Nstep = 200
Nwalk = 3000

x = np.zeros(Nstep)
y = np.zeros(Nstep)
xfinal, yfinal, finald = [], [], []

for j in range(Nwalk):
    for i in range(1, Nstep):
        val = random.Categorical(*[0.45]*8)
        x[i] = x[i - 1] + (val == 1) - (val == 2)
        y[i] = y[i - 1] + (val == 3) - (val == 4)
    finald.append(np.sqrt(x[Nstep-1]**2 + y[Nstep-1]**2))
    xfinal.append(x[Nstep-1])
    yfinal.append(y[Nstep-1])

xbias = np.zeros(Nstep)
ybias = np.zeros(Nstep)
xfinalbias, yfinalbias, finaldbias = [], [], []

for j in range(Nwalk):
    for i in range(1, Nstep):
        val = random.Categorical(*[random.TruncExp(1., 0., 1.)]*3)
        xbias[i] = xbias[i - 1] + (val == 1) - (val == 2)
        ybias[i] = ybias[i - 1] + (val == 3) - (val == 4)
    finaldbias.append(np.sqrt(xbias[Nstep-1]**2 + ybias[Nstep-1]**2))
    xfinalbias.append(xbias[Nstep-1])
    yfinalbias.append(ybias[Nstep-1])

plt.plot(xfinal, yfinal, 'p', color='blue')
plt.grid(True, alpha=0.90)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Final positions after {} random walks'.format(Nwalk))
plt.show()

f1 = np.linspace(0.0, 25.0, 1000)
f2 = 2*f1/Nstep * np.exp(-f1**2/Nstep)
plt.plot(f1, f2, color='red', linestyle='dashed', label='Rayleigh distribution, N={}'.format(Nstep))
n, bins, patches = plt.hist(finald, 15, density=True, color='green', alpha=0.6, fill=True, hatch='/', histtype='step', linewidth=1, label='data')
plt.legend(loc='upper right')
plt.title('Comparison between Data and Rayleigh distributions')
plt.xlabel('r')
plt.ylabel('Probability')
plt.grid(True, alpha=0.90)
plt.show()

plt.plot(xfinalbias, yfinalbias, 'p', color='blue')
plt.grid(True, alpha=0.90)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Final positions after {} random walks'.format(Nwalk))
plt.show()

plt.plot(f1, f2, color='black', linestyle='dashed', label='Rayleigh distribution, N={}'.format(Nstep))
n, bins, patches = plt.hist(finaldbias, 15, density=True, color='purple', alpha=0.6, fill=True, hatch='/', histtype='step', linewidth=1, label='data')
plt.legend(loc='upper right')
plt.title('Comparison between Data and Rayleigh distributions')
plt.xlabel('r')
plt.ylabel('Probability')
plt.grid(True, alpha=0.85)
plt.show()
