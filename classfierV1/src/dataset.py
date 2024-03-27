import os

from PIL import Image

from torch.utils.data import Dataset
from src.utils import CLASSES


class Bread3Dataset(Dataset):
    def __init__(self, image_dir, transform):
        super().__init__()

        self.image_dir = image_dir
        self.transform = transform  # 데이터 전처리를 위한 변환 파이프 라인을 변수에 저장

        self.image.labels = []
        for filename in os.listdir(image_dir):
            label = filename.split('_')[0]
            self.image_labels.append((filename, label))

    def __len__(self):
        return len(self.image_labels)

    def __getitem__(self, index):
        filename, label = self.image_labels[index]
        image_path = os.path.join(self.image_dir, filename)
        image = Image.open(image_path).convert('RGB')

        if self.transform:
            image = self.transform(image)

        label_index = CLASSES.index(label)

        return image, label_index
