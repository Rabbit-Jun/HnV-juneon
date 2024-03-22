import torch

x= torch.randn(2, 3, 2, 2)
# print(x)

flat_x = torch.flatten(x, 1)
print(flat_x)

b =torch.randn(2,12)
print(f'b: {b}')

c = torch.rand(2, 12)
print(f'c:{c}')