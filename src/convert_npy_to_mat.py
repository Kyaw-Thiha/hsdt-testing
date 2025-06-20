import numpy as np
from scipy.io import savemat


def convert_npy_to_mat(input_file_path: str, output_file_path: str, key: str):
    data = np.load(input_file_path)

    savemat(output_file_path, {key: data})
    print("Conversion Successful!")


if __name__ == "__main__":
    convert_npy_to_mat("../data/cuprite512.npy", "../data/clean/Cuprite.mat", "cuprite")
