import torch



print("Torch CUDA: ", torch.cuda.is_available())
device = torch.device("cuda:0")
print(device)
print(torch.cuda.get_device_name(0))
print(torch.rand(3,3).cuda())
print(torch.rand(5,5).cuda() + torch.rand(5,5).cuda())