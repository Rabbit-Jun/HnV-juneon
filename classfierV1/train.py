import torch
from torchvision import transforms, models
from torch import nn, optim
from torch.utils.data import DataLoader

from src.dataset import Bread3Dataset
from src.utils import split_dataset

from tqdm import tqdm

# gpu를 사용
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f'{device}사용중')


def train_one_epoch(dataloader: DataLoader, device, model: nn.Module,
                    loss_fn: nn.Module, optimizer) -> None:

    size = len(dataloader.dataset)
    model.train()
    for batch, (images, targets) in enumerate(dataloader):
        images = images.to(device)
        targets = targets.to(device)

        preds = model(images)
        loss = loss_fn(preds, targets)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if batch % 100 == 0:
            loss = loss.item()
            current = batch * len(images)
            print(f'loss: {loss:>7f}  [{current:>5d}/{size:>5d}]')


def val_one_epoch(dataloader: DataLoader, device, model: nn.Module, loss_fn: nn.Module) -> (float, float):
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
    accuracy = 100 * correct
    print(f'Test Error: \n Accuracy: {accuracy:>0.1f}%, Avg loss: {test_loss:>8f} \n')

    # 수정된 부분: 검증 손실과 정확도를 반환합니다.
    return test_loss, accuracy

# 학습
def train(device):
    image_dir = 'data/bread'
    train_path, test_path = split_dataset(image_dir)
    batch_size = 16
    num_workers = 0
    num_classes = 3  # 클래스 수
    epochs = 50
    # 데이터셋을 훈련과 테스트로 분할

# 데이터 전처리 파이프 라인
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                             std=[0.229, 0.224, 0.225])
    ])

    training_data = Bread3Dataset(train_path, transform=transform)
    test_data = Bread3Dataset(test_path, transform=transform)

    # DataLoader 생성
    train_dataloader = DataLoader(training_data, batch_size=batch_size,
                                  num_workers=num_workers)
    test_dataloader = DataLoader(test_data, batch_size=batch_size,
                                 num_workers=num_workers)
    # 모델 맞추기
    model = models.efficientnet_b3(pretrained=True)
    model.classifier = nn.Linear(in_features=1536, out_features=num_classes)
    model.to(device)

    loss_fn = nn.CrossEntropyLoss()
    optimizer = optim.SGD(model.parameters(), lr=1e-4)

    train_losses = []
    val_losses = []
    val_accuracies = []

    best_accuracy = 0.0
    best_epoch = 0

    for epoch in tqdm(range(epochs), desc='Epochs'):
        print(f'Epoch {epoch + 1}\n-------------------------------')
        train_loss = train_one_epoch(train_dataloader, device, model, loss_fn, optimizer)
        val_loss, val_accuracy = val_one_epoch(test_dataloader, device, model, loss_fn)
        print(f'Validation Loss: {val_loss:.4f}, Accuracy: {val_accuracy:.4f}')

        train_losses.append(train_loss)
        val_losses.append(val_loss)
        val_accuracies.append(val_accuracy)

        if val_accuracy > best_accuracy:
            best_accuracy = val_accuracy
            best_epoch = epoch + 1
            torch.save(model.state_dict(), 'densenet121_best_model_2.pth')
    print(f'Best Validation Accuracy: {best_accuracy:.4f} at Epoch {best_epoch}')
    

    # 모델 저장
    torch.save(model.state_dict(), 'densenet-Bread3_2.pth')
    print("Saved PyTorch Model State to densenet-bread3.pth")


if __name__ == '__main__':
    train(device)
````