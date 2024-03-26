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
        return self.img_url

    def down(self):
        if not os.path.exists(self.bread[0]):
            os.makedirs(self.bread[0])

        img_get = requests.get(self.img_url)
        if img_get.status_code == 200:
            for i, url in enumerate(self.img_url):
                file_path = os.path.join(self.bread[0],
                                         f'{self.bread[i]}_{i}.jpg')
                with open(file_path, 'wb') as f:
                    f.write(img_get.content)

    def run_all(self):
        self.get_url()
        self.crawling()
        self.down()


img_down = Download_Img()
img_down.run_all()
