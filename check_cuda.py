import torch

device = torch.device("cuda:1" if torch.cuda.is_available() else "cpu")
print("Device: ", device)
print("Current cuda device:", torch.cuda.current_device())
print("Count of using GPUs", torch.cuda.device_count())
