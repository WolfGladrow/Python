# file: NeutrinosMeanPoissonLog.py

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson
from datetime import datetime

print("file: NeutrinosMeanPoissonLog.py")
print(datetime.now())

# neutrinos: calculate sample mean and compare relative frequencies with Poisson probabilities

k = np.arange(0, 10)  # number of events (neutrinos in 10 s intervals)
frequencies = np.array([1042, 860, 307, 78, 15, 3, 0, 0, 0, 1])  # frequencies

# Estimate of mean rate = E[k]
lambdaEst = np.sum(k * frequencies) / np.sum(frequencies)
print(round(lambdaEst, 3), "lambdaEst")

# Relative frequencies
rf = frequencies / np.sum(frequencies)

lambdaEst2 = np.sum(k * rf)
print(round(lambdaEst2, 3), "lambdaEst2")

lambdaEst3 = np.sum((k - lambdaEst2) ** 2 * rf)
print(round(lambdaEst3, 3), "lambdaEst3")

# Probabilities based on estimated lambda
pPredict = poisson.pmf(k, lambdaEst)

q = rf / pPredict  # not plotted but kept for completeness

sflag = 3

if sflag == 3:  # log-y plot
    plt.figure(figsize=(6, 6))
    
    # Plot relative frequencies
    plt.plot(k, rf, 'o', color='black', markersize=4)
    plt.yscale('log')
    plt.ylim(1e-7, 1)
    
    plt.xlabel('Number of events, k', fontsize=12)
    plt.ylabel('Probability, relative frequency', fontsize=12)
    
    # Plot Poisson prediction
    plt.plot(k, pPredict, '^', color='magenta', markersize=4)
    
    lambdar = round(lambdaEst, 3)
    # plt.text(5.6, 0.2, r'$\hat{\lambda} =
    plt.text(5.6, 0.2, r'$\hat\lambda = {}$'.format(lambdar),
             color='magenta', fontsize=12)
    
    plt.show()
# NeutrinosLog260222.png