from scipy.io import loadmat, savemat
import os
import numpy as np


FILE_PATH = "../data"


def change_key_of_mat(input_dir: str, output_dir: str):
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
                savemat(os.path.join(output_dir, fname), {"input": img})


if __name__ == "__main__":
    change_key_of_mat(f"{FILE_PATH}/raw", f"{FILE_PATH}/clean")
