from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
import time


class WebCrawling:
    def __init__(self, urls, bread):
        self.urls = urls
        self.bread = bread
        self.driver = webdriver.Chrome()
        self.src_values = []
        self.end_point = False
        self.driver.implicitly_wait(10)

        # 웹 사이트 열기
    def open_web(self, url):
        self.driver.get(url)
        # 웹 페이지의 alt속성값이 bread와 일치하는 src를 찾는다
        time.sleep(1)

    def find_src(self, keyword):
        time.sleep(1)
        img_tags = self.driver.find_elements(By.TAG_NAME, "img")
        self.src_values = [img.get_attribute("src") for img in img_tags
                           if keyword in img.get_attribute("alt")]

        # 스크롤 내리기
    def scroll_down(self):
        scroll_origin = ScrollOrigin.from_viewport(10, 10)

        ActionChains(self.driver)\
            .scroll_from_origin(scroll_origin, 0, 1000)\
            .perform()

    # end 포인트를 찾기위한 함수
    def find_end(self):
        end_find = self.driver.find_elements(By.TAG_NAME, "div")
        for end in end_find:
            if end.text == '더 이상 표시할 콘텐츠가 없습니다.':
                self.end_point = True
                break

        # 더보기가 나오면 클릭
    def click_seemore(self):
        try:
            see_more = self.driver.find_elements(By.TAG_NAME, "input")
            for input_tag in see_more:
                if input_tag.get_attribute('value') == "결과 더보기":
                    input_tag.click()
                    break
        except Exception as e:
            print("더보기 버튼을 찾을 수가 없습니다", e)

    def close_web(self):
        self.driver.quit()

    def run_all(self):
        for url, keyword in zip(self.urls, self.bread):
            self.open_web(url)
            while True:
                self.find_src(keyword)
                self.scroll_down()
                self.click_seemore()
                self.scroll_down()
                self.find_end()
                if self.end_point:
                    break

        self.close_web()
