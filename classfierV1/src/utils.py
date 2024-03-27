import os
import shutil
import random

CLASSES = [
    'baguette',
    'soboro',
    'bread'
]


def split_dataset(image_dir: os.PathLike, split_rate: float = 0.2) -> None:
    # 이미지 목록 가져오기
    files = [f for f in os.listdir(image_dir)
             if os.path.isfile(os.path.join(image_dir, f))]
    random.shuffle(files)

    # 몇번 인덱스에서 분할하지 정하기
    split_point = int(len(files) * split_rate)

    # 테스트 파일과 훈련파일로 나눔
    test_files = files[:split_point]
    train_files = files[split_point:]

    # 후련, 테스트 폴더 생성
    train_dir = os.pathjoin(image_dir, 'train')
    test_dir = os.path.join(image_dir, 'test')
    os.makedirs(image_dir, "tratin", exist_ok=True)
    os.makedirs(image_dir, "test", exist_ok=True)

    # 파일을 각각의 폴더로 이동
    for file in train_files:
        shutil.move(os.path.join(image_dir, file), os.path.join(train_dir,
                                                                file))
    for file in test_files:
        shutil.move(os.path.join(image_dir, file), os.path.join(test_dir,
                                                                file))
