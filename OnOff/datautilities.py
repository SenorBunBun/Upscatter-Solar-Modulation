from scipy import integrate
import numpy as np
from math import sin, pi

# min1 = 30
# max1 = 50
# list1 = np.arange(15, 100)
# dict1 = {"a": [list1, list1], "b": [list1, list1]}

def pdintegratedict(dictdata, minh, maxh):
    total = 0
    for entry in dictdata:
        templistx = dictdata[entry][0]
        templisty = dictdata[entry][1]

        # print(templistx)
        # print(templisty)

        indexInRange = np.where((templistx >= minh) & (templistx <= maxh))[0]

        if len(indexInRange) > 0:
            print("True" + str(indexInRange))
            # print("Index of Range :" + str(indexInRange))
            # print("Index of Range last index:" + str(indexInRange[-1]))
            total += integrate.simpson(templisty[indexInRange[0]: indexInRange[-1] + 1], templistx[indexInRange[0]: indexInRange[-1] + 1])

    return total

def signalintegral(amplitude, binstart, binend):
    def modulation(x):
        return amplitude * sin( (pi/12)*x + pi/2) + amplitude
    return integrate.quad(modulation, binstart, binend)


# print(pdintegratedict(dict1, min1, max1))
# print("\n Good Stuff")
# output = np.where((list1 > min1) & (list1 < max1))[0]
# print(list1)
# print(output)
