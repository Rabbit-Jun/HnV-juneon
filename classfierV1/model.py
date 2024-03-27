import torch
from torchvision import transforms, models
from PIL import Image
import os

# 모델 초기화
alexnet = models.alexnet(pretrained=True) # 사전 훈련된 AlexNet 사용

# 전처리 파이프라인 정의
preprocess = transforms.Compose([
    transforms.Resize(256),  # 먼저 이미지 크기를 조정
    transforms.CenterCrop(224), # 이미지 중앙에서 224x224 크기로 자름
    transforms.ToTensor(),  # 이미지를 텐서로 변환
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),  # 정규화
])

# 이미지 로드 및 전처리
data_path = "./data/baguette"
for i in len(os.listdir(data_path)):
    img = Image.open(f'./data/baguette/{i}')  # 이미지 경로와 파일명 수정
    img_t = preprocess(img)
    batch_t = torch.unsqueeze(img_t, 0)  # 배치 차원 추가

# 모델에 이미지 넣고 출력 받기
output = alexnet(batch_t)

# 결과 처리
# output에 대한 처리 코드 추가 (예: 분류 결과 해석)
