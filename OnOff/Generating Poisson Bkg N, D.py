import numpy as np
import pandas as kfp
from datetime import datetime

# Bkg Mean Taking from Integration
bkgmean = 246.46183123942518

# Have to replace : because windows doesn't allow in filename
directory = "C:/Users/suria/Creations/Fermilab/Upscatter-Solar-Modulation/OnOff/{0}/PoissonNoSig1Day_{1}.csv".format('Generated Data', str(datetime.now()).replace(':', "") )


def genpoisson(mean, size=1):
    return np.random.poisson(mean, size)


nosigData = kfp.DataFrame({'Night': genpoisson(bkgmean), 'Day':genpoisson(bkgmean)})
nosigData.to_csv(directory)