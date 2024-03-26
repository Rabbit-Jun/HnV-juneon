from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.common.exceptions import NoSuchElementException, \
    JavascriptException, StaleElementReferenceException
import time


class WebCrawling:
    def __init__(self, urls, bread):
        self.urls = urls
        self.bread = bread
        self.driver = webdriver.Chrome()
        self.src_values = []
        self.footer_found = False

        # 웹 사이트 열기
    def open_web(self, url):
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        # 웹 페이지의 alt속성값이 bread와 일치하는 src를 찾는다

    def find_src(self, keyword):
        img_tags = self.driver.find_elements(By.TAG_NAME, "img")
        self.src_values = [img.get_attribute("src") for img in img_tags
                           if keyword in img.get_attribute("alt")]

        # 스크롤 내리기
    def scroll_down(self):
        try:

            scroll_origin = ScrollOrigin.from_viewport(10, 10)

            ActionChains(self.driver)\
                .scroll_from_origin(scroll_origin, 0, 1000)\
                .perform()
            time.sleep(2)

        except NoSuchElementException:
            footer = self.driver.find_element(By.TAG_NAME, "footer")
            ActionChains(self.driver)\
                .scroll_to_element(footer)\
                .perform()
            self.footer_found = True

        except JavascriptException:
            pass
        except StaleElementReferenceException:
            pass

        # 더보기가 나오면 클릭
    def click_seemore(self):
        try:
            see_more = self.driver.find_element(By.CLASS_NAME, "button")
            see_more.click()
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
                if self.footer_found:
                    break

        self.close_web()


urls = list(input('이미지를 다운로드하기 위한 주소를 입력해주세요: ').split(' '))
bread = list(input('이미지를 구별하기 위한 키워드를 입력해주세요: ').split(' '))

crawling = WebCrawling(urls, bread)
crawling.run_all()
print(crawling.src_values)
