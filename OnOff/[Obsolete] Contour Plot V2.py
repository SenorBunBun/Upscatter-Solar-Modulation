import pandas as kfp
import scipy.interpolate as interp
import scipy.ndimage as nd
import datautilities
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker, cm


unprocessedSig = kfp.read_csv("Signal Data/rateTable.csv", header=None)
dipoletoAmplitude = { }

for index in range(len(unprocessedSig)):
    dipoletoAmplitude[ unprocessedSig[1][index] ] = unprocessedSig[2][index]
numofmasses = 11
fulldict = {}

for index in range(1, int(len(unprocessedSig[0])/numofmasses) + 1 ):
    # print(index*numofmasses)
    fulldict[ unprocessedSig[0][index*numofmasses - 1] ] = dipoletoAmplitude


print(datautilities.signalintegral(1, 6, 18))

# [X, Y] = np.meshgrid(unprocessedSig[0][0:4], unprocessedSig[1][0:4])
# [X, Y] = np.meshgrid(unprocessedSig[0], unprocessedSig[1])
# [X, Y] = np.meshgrid(nd.zoom(unprocessedSig[0], 5), nd.zoom(unprocessedSig[1], 20))
 masspoints = np.linspace(0.5, 7.5, )

massvals = np.array(unprocessedSig[0])
dipolevals = np.array(unprocessedSig[1])
amplitudevalsy = np.array(unprocessedSig[2])

# Ti = interp.griddata( (massarray, dipolearray), amplitudearray, (X, Y), method='cubic')
# plt.contourf(X, Y, Ti, locator=ticker.LogLocator())

# plt.yscale('log')
# plt.xscale('log')
plt.title("Contour Plot: Expected Number of Events in 24 hours | Mass and $d_{n}$ ", y=1.05)
plt.ylabel('Dipole Coupling Strength ($d_{N}$)')
plt.xlabel('Mass (meV)')
plt.tight_layout()
plt.legend()
plt.show()