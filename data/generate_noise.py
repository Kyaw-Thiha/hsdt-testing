import os

from glob import glob
import scipy
import h5py
import numpy as np


def add_gaussian_noise(input_dir: str, output_dir: str, sigma: int):
    print("adding noise")
    os.makedirs(output_dir, exist_ok=True)
    mat_files = glob(os.path.join(input_dir, "*.mat"))
    i = 0
    print("go")

    for mat_path in mat_files:
        print(f"Generating Image-{i} for sigma-{sigma}")
        with h5py.File(mat_path, "r") as f:
            key = list(f.keys())[0]  # assume the dataset is the first key
            img = np.array(f[key]).astype(np.float32)
            # print(f"{os.path.basename(mat_path)} shape: {img.shape}")
            img = img.transpose(
                2, 1, 0
            )  # MATLAB to NumPy: (bands, cols, rows) → (rows, cols, bands)

        noisy = img + np.random.normal(0, sigma, img.shape).astype(np.float32)

        save_path = os.path.join(output_dir, os.path.basename(mat_path))
        scipy.io.savemat(save_path, {key: noisy})
        i = i + 1


print("Generating noisy images of Sigma-30")
add_gaussian_noise("icvl_clean", "icvl_30", sigma=30)
print("-------------------------------------")

print("Generating noisy images of Sigma-50")
add_gaussian_noise("icvl_clean", "icvl_50", sigma=50)
print("-------------------------------------")

print("Generating noisy images of Sigma-70")
add_gaussian_noise("icvl_clean", "icvl_70", sigma=70)
print("-------------------------------------")
