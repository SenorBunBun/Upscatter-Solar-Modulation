import numpy as np
from numpy import sqrt, pi, e, inf
import scipy.integrate as integrate
import pandas as kfp
global lambdaon, lambdaoff, lambdabkg

obsdata = kfp.read_csv('Generated Data/PoissonNoSig1Day_2021-07-30 010022.386052.csv', usecols=['Night', 'Day'])
nightobs = float(obsdata['Night'])
dayobs = float(obsdata['Day'])
deltaobs = nightobs - dayobs
sumobs = nightobs + dayobs

lambdaon = 0
lambdaoff = 0
lambdabkg = 246.46183123942518

def deltapdf(delta):
    return (e ** (-0.5 * ( ((delta - (lambdaon - lambdaoff)) ** 2) / (lambdaon + lambdaoff + 2 * lambdabkg) ) )) / ( sqrt(2 * pi * (lambdaon + lambdaoff + 2 * lambdabkg)) )


def a2sigma(con, coff, deltaobs, lambdabkg):
    return (con * (deltaobs + 2) - coff * (deltaobs - 2)) / ((con - coff) ** 2) + (2 * sqrt(2 * lambdabkg * ((con - coff) ** 2) + (con ** 2 + coff ** 2) * deltaobs + coff + con)) / ((con - coff) ** 2)


# Given by Integration
sineCon = (12 * pi + 24) / pi
sineCoff = (12 * pi - 24) / pi

print(integrate.quad(deltapdf, deltaobs, inf))
print(a2sigma(sineCon, sineCoff, deltaobs, lambdabkg))