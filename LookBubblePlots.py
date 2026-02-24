# file: LookBubblePlots.py
# Data source: Borcard et al. (2011)

import numpy as np
import matplotlib.pyplot as plt

# Data
x = np.array([88,94,102,100,106,112,114,110,136,168,186,205,222,228,252,266,245,225,
              206,189,187,192,192,179,145,91,65,49,27,8])

y = np.array([7,14,18,28,39,51,61,76,100,112,130,145,167,182,190,209,203,200,
              194,193,201,212,228,233,217,187,174,164,151,133])

NO3g = np.array([0.20,0.20,0.22,0.21,0.52,0.15,0.15,0.41,0.82,0.75,1.60,0.50,0.52,1.23,
                 1.00,2.00,2.50,2.20,2.20,3.00,2.20,1.62,3.50,2.50,6.20,3.00,3.00,4.00,1.62,1.60])

# Convert from mg/L to µmol/L: HNO3 molar mass = 63 g/mol
NO3 = NO3g * 1000 / 63  # µmol/L

# Create figure with two subplots
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# --- First plot: radius proportional to NO3 ---
sizes1 = (5 * NO3 / np.max(NO3))**2 * 100  # squared for area scaling in matplotlib
axes[0].scatter(x, y, s=sizes1, facecolors='brown', edgecolors='white')
axes[0].plot(x, y, color='blue')
axes[0].set_xlim(0, 300)
axes[0].set_ylim(0, 300)
axes[0].set_xlabel('x (km)', fontsize=12)
axes[0].set_ylabel('y (km)', fontsize=12)
axes[0].text(0, 280, r'$r = NO_3\, (\mu mol/L)$', color='brown', fontsize=12)

# --- Second plot: radius proportional to sqrt(NO3) ---
sizes2 = (5 * np.sqrt(NO3 / np.max(NO3)))**2 * 100
axes[1].scatter(x, y, s=sizes2, facecolors='brown', edgecolors='white')
axes[1].plot(x, y, color='blue')
axes[1].set_xlim(0, 300)
axes[1].set_ylim(0, 300)
axes[1].set_xlabel('x (km)', fontsize=12)
axes[1].set_ylabel('y (km)', fontsize=12)
axes[1].text(0, 280, r'$r = \sqrt{NO_3\, (\mu mol/L)}$', color='brown', fontsize=12)

plt.tight_layout()
plt.show()
# BubblePlotRadiusAndArea260224.png
# Notes on Differences from R:
# In matplotlib, s controls marker area, not radius.
# Therefore we square the scaling term to mimic R’s cex (which scales radius).
# LaTeX formatting works directly using raw strings (r'...').
# Figure size is approximated (R used 16 cm × 16 cm).