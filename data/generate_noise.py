import os

import glob
import scipy
import numpy as np

for sigma in [30, 50]:
    os.makedirs(f"icvl_{sigma}", exist_ok=True)
    i = 0
    for f in glob.glob("icvl_clean/*.mat"):
        print(f"Generating Image-{i} for sigma-{sigma}")
        data = scipy.io.loadmat(f)["img"]
        noisy = data + np.random.randn(*data.shape) * sigma
        scipy.io.savemat(f"icvl_{sigma}/{os.path.basename(f)}", {"img": noisy})
        i = i + 1
