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

# print(fulldict[0.05][5.016891464581947e-12])

print(datautilities.signalintegral(1, 6, 18))

# [X, Y] = np.meshgrid(unprocessedSig[0][0:4], unprocessedSig[1][0:4])
[X, Y] = np.meshgrid(unprocessedSig[0], unprocessedSig[1])
[X, Y] = np.meshgrid(nd.zoom(unprocessedSig[0], 5), nd.zoom(unprocessedSig[1], 20))

# print("X, Y")
# print(X)
# print("X End")
# print(Y)

#pol.griddata([unprocessedSig[0], unprocessedSig[1]], unprocessedSig[2], (X, Y), method='nearest')

massarray = np.array(unprocessedSig[0])
dipolearray = np.array(unprocessedSig[1])
amplitudearray = np.array(unprocessedSig[2])

# def f(x, y):
#    return x + y
# print("F(x)")
# print(array)
# print(f(array, array))

# print(np.random.choice(unprocessedSig[0][0:4], len(unprocessedSig[0][0:4])))
dailyrate = []
# print(datautilities.signalintegral(1, 6, 32))
for data in range( len(unprocessedSig[2]) ):
    temprate = datautilities.signalintegral(unprocessedSig[2][data], 6, 30)[0]
    # print(temprate)
    dailyrate.append(temprate)

dailyratearray = np.array(dailyrate)
# print(dailyratearray)

dailyratearray.sort()
# print(dailyratearray)

# massarray = nd.zoom(massarray, 5)
# dipolearray = nd.zoom(dipolearray, 5)
# amplitudearray = nd.zoom(amplitudearray, 5)


Ti = interp.griddata( (massarray, dipolearray), amplitudearray, (X, Y), method='linear')
plt.contourf(X, Y, Ti, locator=ticker.LogLocator())

# plt.yscale('log')
# plt.xscale('log')
plt.title("Contour Plot: Expected Number of Events in 24 hours | Mass and $d_{n}$ ", y=1.05)
plt.ylabel('Dipole Coupling Strength ($d_{N}$)')
plt.xlabel('Mass (meV)')
plt.tight_layout()
plt.legend()
plt.show()