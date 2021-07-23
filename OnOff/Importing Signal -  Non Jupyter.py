import pandas as kfp
import datautilities
import numpy as np

unprocessedSig = kfp.read_csv("Signal Data/rateTable.csv", header=None)
dipoletoAmplitude = { }

for index in range(len(unprocessedSig)):
    dipoletoAmplitude[ unprocessedSig[1][index] ] = unprocessedSig[2][index]
numofmasses = 11
fulldict = {}

for index in range(1, int(len(unprocessedSig[0])/numofmasses) + 1 ):
    print(index*numofmasses)
    fulldict[ unprocessedSig[0][index*numofmasses - 1] ] = dipoletoAmplitude

print(fulldict[0.05][5.016891464581947e-12])

print(datautilities.signalintegral(1, 0, 12))






