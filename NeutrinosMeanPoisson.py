import numpy as np
import matplotlib.pyplot as plt
import scipy
import scipy.stats as stats
from scipy.stats import poisson
from datetime import datetime


print("file: NeutrinosMeanPoisson.py")
print(datetime.now())

# neutrinos: calculate sample mean and compare relative frequencies with Poisson probabilities

k = np.arange(0, 10)  # number of events (neutrinos in 10 s intervals)
frequencies = np.array([1042, 860, 307, 78, 15, 3, 0, 0, 0, 1])  # frequencies

# estimate of mean rate = E[k]
lambdaEst = np.sum(k * frequencies) / np.sum(frequencies)
print(round(lambdaEst, 3), "lambdaEst")

# relative frequencies
rf = frequencies / np.sum(frequencies)

lambdaEst2 = np.sum(k * rf)
print(round(lambdaEst2, 3), "lambdaEst2")

lambdaEst3 = np.sum((k - lambdaEst2) ** 2 * rf)
print(round(lambdaEst3, 3), "lambdaEst3")

# probabilities based on estimated lambda
pPredict = poisson.pmf(k, lambdaEst)

q = rf / pPredict

sflag = 2

if sflag == 2:
    plt.figure()
    plt.plot(k, rf, 'o', color='black', markersize=4)
    plt.xlabel("Number of events, k", fontsize=12)
    plt.ylabel("Probability, relative frequency", fontsize=12)
    
    plt.plot(k, pPredict, marker='^', linestyle='None',
             color='magenta', markersize=4)

    lambdar = round(lambdaEst, 3)
    # plt.text(5.6, 0.2, '$\hat{\lambda} = {}$'.format(lambdar),
    #       color='magenta', fontsize=14)
    
    # DWG: note \hat{\lambda} replaced by \hat\lambda
    
    plt.text(5.6, 0.2, r'$\hat\lambda = {}$'.format(lambdar),
             color='magenta', fontsize=14)
    #plt.text(5.6, 0.2, r'$\hat{\lambda} = {}$'.format(lambdar),
    #        color='magenta', fontsize=14)

    plt.show()
    # KeyError: '\\lambda'
    # NeutrinosP260222.png