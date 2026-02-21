print('file: PDsPDFsPoisson2Examples.py')

import numpy as np
import matplotlib.pyplot as plt
# pip install scipy
import scipy
import scipy.stats as stats
# print(scipy.__version__)          # see what version you have
# help(stats)  
from scipy.stats import poisson

lambda1 = 0.55
lambda2 = 3.72

k = np.arange(0, 11)

p1 = poisson.pmf(k, lambda1)
p2 = poisson.pmf(k, lambda2)

plt.figure()

# First Poisson distribution
plt.plot(k, p1, 'o', color='black', markersize=6, label=f'λ1 = {lambda1}')

# Second Poisson distribution
plt.plot(k, p2, '^', color='magenta', markersize=6, label=f'λ2 = {lambda2}')

plt.xlabel('k', fontsize=14)
plt.ylabel('Poisson probability distributions', fontsize=14)
plt.tick_params(axis='both', labelsize=10)

plt.text(3, 0.5,  f'λ₁ = {lambda1}', color='black', fontsize=14)
plt.text(3, 0.4,  f'λ₂ = {lambda2}', color='magenta', fontsize=14)

plt.legend()
plt.show()
# PoissonPDsEx260221Py.png