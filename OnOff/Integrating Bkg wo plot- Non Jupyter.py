from scipy import integrate
import numpy as np
import pandas as kfp

# min1 = 30
# max1 = 50
# list1 = np.arange(15, 100)
# dict1 = {"a": [list1, list1], "b": [list1, list1]}

allbkg = {
    "Bi210": kfp.read_csv("bkgs/Bi210.csv", header=None),
    "C11": kfp.read_csv("bkgs/C11.csv", header=None),
    "C14": kfp.read_csv("bkgs/C14.csv", header=None),
    "Kr85": kfp.read_csv("bkgs/Kr85.csv", header=None),
    "Po210": kfp.read_csv("bkgs/Po210.csv", header=None),
    "Pile Up": kfp.read_csv("bkgs/pile_up.csv", header=None),
    "Ext Bkg 1": kfp.read_csv("bkgs/ext_bkg_1.csv", header=None),
    "Ext Bkg 2" : kfp.read_csv("bkgs/ext_bkg_2.csv", header=None),
    "Ext Bkg 3": kfp.read_csv("bkgs/ext_bkg_3.csv", header=None),

    "B8" : kfp.read_csv("bkgs/solar n/B8.csv", header=None),
    "Be7" : kfp.read_csv("bkgs/solar n/Be7.csv", header=None),
    "CNO" : kfp.read_csv("bkgs/solar n/CNO.csv", header=None),
    "Pep" : kfp.read_csv("bkgs/solar n/pep.csv", header=None),
    "Pp" : kfp.read_csv("bkgs/solar n/pp.csv", header=None)

}

print(allbkg['Bi210'])

# Hits Corresponding to 300 KeV
minhits = 134.09523809523805

# Hits Corresponding to 500 KeV
maxhits = 211.42857142857142

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

print(pdintegratedict(allbkg, minhits, maxhits))

# print(pdintegratedict(dict1, min1, max1))
# print("\n Good Stuff")
# output = np.where((list1 > min1) & (list1 < max1))[0]
# print(list1)
# print(output)
