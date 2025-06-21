from scipy.io import loadmat, savemat
import os
import numpy as np


FILE_PATH = "../data"


def clean_mat(input_dir: str, output_dir: str):
    """
    A function that clean the mat files from the `input_dir`,
    and save the clean versions in the `output_dir`
    Currently, it does
    - Change the main key to be 'input'
    - Add a key called 'gt' meant to act as a ground_truth
    !!! Ensure gt is not changed when adding noise
    """
    os.makedirs(output_dir, exist_ok=True)

    for fname in os.listdir(input_dir):
        if not fname.endswith(".mat"):
            continue
        data = loadmat(os.path.join(input_dir, fname))

        for key, value in data.items():
            if key.startswith("__"):
                continue
            if isinstance(value, np.ndarray):
                img = data.get(key)
                savemat(
                    os.path.join(output_dir, fname),
                    {"input": img, "gt": img},
                )
        print(f"[✓] Cleaned and saved: {fname}")


if __name__ == "__main__":
    print(f"Cleaning the files from {FILE_PATH}")
    clean_mat(f"{FILE_PATH}/raw", f"{FILE_PATH}/clean")
    print("-------------------------------------")
