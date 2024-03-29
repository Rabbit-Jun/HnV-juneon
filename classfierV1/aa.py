from torchvision import transforms, models

model = models.efficientnet_b3(pretrained=True)
print(model)
