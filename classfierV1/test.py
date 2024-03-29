import torch
from torchvision import transforms
from torch.utils.data import DataLoader
from src.dataset import Bread3Dataset
from src.utils import CLASSES
from torch import nn, optim
from torchvision import models

def test(model, device, dataloader, loss_fn):
    size = len(dataloader.dataset)
    num_batches = len(dataloader)
    model.eval()
    test_loss, correct = 0, 0
    with torch.no_grad():
        for images, targets in dataloader:
            images = images.to(device)
            targets = targets.to(device)
            preds = model(images)
            test_loss += loss_fn(preds, targets).item()
            correct += (preds.argmax(1) == targets).type(torch.float).sum().item()
    test_loss /= num_batches
    correct /= size
    print(f"Test Error: \n Accuracy: {(100*correct):>0.1f}%, Avg loss: {test_loss:>8f} \n")

def main():
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Using {device}")

    # 데이터 전처리 파이프라인
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                             std=[0.229, 0.224, 0.225])
    ])

    # 테스트 데이터셋 로드
    test_data = Bread3Dataset('data/bread/test', transform=transform)
    test_dataloader = DataLoader(test_data, batch_size=32, num_workers=4)

    # 모델 설정
    num_classes = 3
    model = models.densenet121(pretrained=True)
    model.classifier = nn.Linear(model.classifier.in_features, num_classes)
    model.to(device)

    # 모델 상태 로드
    model.load_state_dict(torch.load('densenet121_best_model_1.pth', map_location=device))

    # 손실 함수 및 최적화 알고리즘 설정
    loss_fn = nn.CrossEntropyLoss()

    # 테스트 실행
    test(model, device, test_dataloader, loss_fn)

if __name__ == "__main__":
    main()
