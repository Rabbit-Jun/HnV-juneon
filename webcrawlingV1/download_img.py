from webcrawling import WebCrawling
import requests
import os


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
        # 디렉토리가 존재하지 않으면 생성
        folder_name = self.bread[0] if self.bread else "default_folder"
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        for i, url in enumerate(self.img_url):
            img_get = requests.get(url)  # 각 URL에 대한 요청
            if img_get.status_code == 200:
                # 파일 이름이 중복되지 않도록 경로 설정
                file_path = os.path.join(folder_name,
                                         f'{self.bread[0]}_{i}.jpg')
                with open(file_path, 'wb') as f:
                    f.write(img_get.content)  # 응답 내용을 파일에 저장

    def run_all(self):
        self.get_url()
        self.crawling()
        self.down()


img_down = Download_Img()
img_down.run_all()
