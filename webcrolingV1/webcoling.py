from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class webcroling:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome()
    

    def open_web(self):
        # 웹 사이트 열기
        self.driver.get(self.url)

        while True:
            # <div>의 값을 확인
            end = driver.find_element(By.CSS_SELECTOR, ".OuJzKb.Yu2Dnd")
            # 웹 페이지의 alt속성값 저장
            img_tags = driver.find_elements(By.TAG_NAME, "img")
            for img_alt in img_tags:
                img_alt = img_alt.get_attribute("alt")
                # print(img_alt)

            # 스콜 내려서 더 많은 alt 속성값 얻기
            ActionChains(driver)\
                .scroll_to_element(end)\
                .perform()

            # <div>값이 더 이상 표시할 콘텐츠가 없습니다면 멈추기
            if end == '더 이상 표시할 콘텐츠가 없습니다':
            


        # 브라우저 닫기 (자원을 해체하고 메모리 누수 방지)
        driver.quit()


url = 'https://www.google.com/search?sca_esv=5317fe2df48c7\
    1c4&q=%EC%8B%9D%EB%B9%B5&tbm=isch&source=lnms&prmd=isvm\
        nbz&sa=X&ved=2ahUKEwiaqvTdqYyFAxVIh1YBHdtsC54Q0pQJeg\
            QIDxAB&biw=678&bih=1269&dpr=1'

webcroling(url)