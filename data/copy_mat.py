import os
import shutil

# Define source and target directories
source_dir = "HS"
target_dir = "icvl_clean"

# Create the target directory if it doesn't exist
os.makedirs(target_dir, exist_ok=True)

# Loop over all files in the source directory
for root, _, files in os.walk(source_dir):
    for file in files:
        if file.lower().endswith(".mat"):
            src_path = os.path.join(root, file)
            dst_path = os.path.join(target_dir, file)
            shutil.copy2(src_path, dst_path)
            print(f"Copied: {src_path} → {dst_path}")
