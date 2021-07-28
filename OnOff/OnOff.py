import numpy as np
from numpy import sqrt, pi, e, inf
import scipy.integrate as integrate
import datautilities

nightobs, dayobs = (1, 1)
deltaobs = nightobs - dayobs
sumobs = nightobs + dayobs


def deltapdf(lambdaon, lambdaoff, lambdabkg, delta):
    return (1 / sqrt(2 * pi * (lambdaon + lambdaoff + 2 * lambdabkg) )) * (e ** ( ((delta - (lambdaon - lambdaoff) ) ** 2) / (-2 * (lambdaon + lambdaoff + 2 * lambdabkg)) ))

lambdaon = 0
lambdaoff = 0
lambdabkg = 1
print(integrate.quad(deltapdf, deltaobs, np.inf, args=(lambdaon, lambdaoff, lambdabkg)))

con = (pi + 2) / (2 * pi)
coff = (pi - 2) / (2 * pi)

def A2sigma(con, coff, deltaobs, lambdabkg):
    return (con * (deltaobs + 2) - coff*(deltaobs - 2))/ ((con-coff) ** 2) + (2 * sqrt(2*lambdabkg*((con - coff)** 2) + (con ** 2 + coff ** 2) * deltaobs + coff + con) ) / ((con - coff) ** 2)

print(A2sigma(con, coff, deltaobs, lambdabkg))