import torch

ckpt = torch.load("../models/hsdt_l_complex.pth", map_location="cpu")
print(ckpt.keys())
