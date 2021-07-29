import numpy as np
from numpy import sqrt, pi, e, inf
import scipy.integrate as integrate
import datautilities

global lambdaon, lambdaoff, lambdabkg

nightobs, dayobs = (1, 1)
deltaobs = nightobs - dayobs
sumobs = nightobs + dayobs

lambdaon = 0
lambdaoff = 0
lambdabkg = 1
tempdelta = 1

def deltapdf(delta):
    # return (1 / sqrt(2 * pi * (lambdaon + lambdaoff + 2 * lambdabkg) )) * (e ** ( ((delta - (lambdaon - lambdaoff) ) ** 2) / (-2 * (lambdaon + lambdaoff + 2 * lambdabkg)) ))
    return (e ** (-0.5 * ( ((delta - (lambdaon - lambdaoff)) ** 2) / (lambdaon + lambdaoff + 2 * lambdabkg) ) )) / ( sqrt(2 * pi * (lambdaon + lambdaoff + 2 * lambdabkg)) )


def A2sigma(con, coff, deltaobs, lambdabkg):
    return (con * (deltaobs + 2) - coff * (deltaobs - 2)) / ((con - coff) ** 2) + (2 * sqrt(2 * lambdabkg * ((con - coff) ** 2) + (con ** 2 + coff ** 2) * deltaobs + coff + con)) / ((con - coff) ** 2)

# print( e ** (-0.5 * ( ((tempdelta - (lambdaon - lambdaoff)) ** 2) / (lambdaon + lambdaoff + 2 * lambdabkg) ) ) )
# print( ( sqrt(2 * pi * (lambdaon + lambdaoff + 2 * lambdabkg)) ) ) print((e ** (-0.5 * ( ((tempdelta - (lambdaon -
# lambdaoff)) ** 2) / (lambdaon + lambdaoff + 2 * lambdabkg) ) )) / ( sqrt(2 * pi * (lambdaon + lambdaoff + 2 *
# lambdabkg)) ))

debugDeltapdf = {0.5: [0, 0, 1, 0],
                 5.47 * (10 ** -6): [0, 0,10, 20]}
debugAmplitude = {0.395: [(12 * pi + 24) / pi, (12 * pi - 24) / pi,  lambdabkg, 0]}

for entry in debugDeltapdf:
    lambdaon = debugDeltapdf[entry][0]
    lambdaoff = debugDeltapdf[entry][1]
    lambdabkg = debugDeltapdf[entry][2]
    tempdelta = debugDeltapdf[entry][3]
    print("Correct Probability :" + str(entry) + " Mine :" + str(integrate.quad(deltapdf, tempdelta, inf)[0]))

for entry in debugAmplitude:
    tempCon = debugAmplitude[entry][0]
    tempCoff = debugAmplitude[entry][1]
    lambdabkg = debugAmplitude[entry][2]
    tempdelta = debugAmplitude[entry][3]
    print("Correct Amplitude :" + str(entry) + " Mine :" + str(A2sigma(tempCon, tempCoff, tempdelta, lambdabkg)))

# print(integrate.quad(deltapdf, deltaobs, inf))

sineCon = (12 * pi + 24) / pi
sineCoff = (12 * pi - 24) / pi


# print(A2sigma(sineCon, sineCoff, deltaobs, lambdabkg))
