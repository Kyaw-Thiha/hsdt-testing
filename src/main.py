from clean_mat import clean_mat
from add_gaussian_noise import add_gaussian_noise
from downsample import load_downsample_save

FILE_PATH = "../data"

OUT_BANDS = 31


def main():
    print(f"Cleaning the files from {FILE_PATH}")
    clean_mat(f"{FILE_PATH}/raw", f"{FILE_PATH}/clean")
    print("-------------------------------------")

    print(f"Downsampling the files from {FILE_PATH}")
    load_downsample_save(
        f"{FILE_PATH}/clean",
        f"{FILE_PATH}/clean",
        keys=["input", "gt"],
        out_bands=OUT_BANDS,
    )
    print("-------------------------------------")

    print("Generating noisy images of Sigma-30")
    add_gaussian_noise(
        f"{FILE_PATH}/clean", f"{FILE_PATH}/noise_gaussian_30", snr_db=30
    )
    print("-------------------------------------")

    print("Generating noisy images of Sigma-50")
    add_gaussian_noise(
        f"{FILE_PATH}/clean", f"{FILE_PATH}/noise_gaussian_50", snr_db=50
    )
    print("-------------------------------------")

    print("Generating noisy images of Sigma-70")
    add_gaussian_noise(
        f"{FILE_PATH}/clean", f"{FILE_PATH}/noise_guassian_70", snr_db=70
    )
    print("-------------------------------------")


if __name__ == "__main__":
    main()
