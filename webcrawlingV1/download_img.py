from webcrawling import WebCrawling
import requests
import os
import base64


class Download_Img:
    def __init__(self):
        self.urls = []
        self.bread = []

    def get_url(self):
        self.urls = list(input('이미지를 다운로드하기 위한 주소를 입력해주세요: ').split(' '))
        self.bread = list(input('이미지를 구별하기 위한 키워드를 입력해주세요: ').split(' '))

    def crawling(self):
        crawling = WebCrawling(self.urls, self.bread)
        crawling.run_all()
        self.img_url = crawling.src_values

    def down(self):
        folder_name = self.bread[0] if self.bread else "default_folder"
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        for i, url in enumerate(self.img_url):
            # 데이터 URL 처리
            if url.startswith('data:image'):
                # 데이터 URL에서 순수 데이터 부분만 추출
                header, encoded = url.split(',', 1)
                data = base64.b64decode(encoded)  # base64 디코딩
                file_path = os.path.join(folder_name,
                                         f'{self.bread[0]}_{i}.jpg')
                with open(file_path, 'wb') as f:
                    f.write(data)  # 파일에 저장
            # 일반 URL 처리
            else:
                img_get = requests.get(url)
                if img_get.status_code == 200:
                    file_path = os.path.join(folder_name,
                                             f'{self.bread[0]}_{i}.jpg')
                    with open(file_path, 'wb') as f:
                        f.write(img_get.content)

    def run_all(self):
        self.get_url()
        self.crawling()
        self.down()


img_down = Download_Img()
img_down.run_all()
