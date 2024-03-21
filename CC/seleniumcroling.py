import requests
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# ChromeDriver 설정
s = Service('./chromedriver.exe')  # 여기를 자신의 ChromeDriver 경로로 수정하세요.
driver = webdriver.Chrome(service=s)
driver.get("https://www.google.com/search?q=%EC%8B%9D%EB%B9%B5&tbm=isch&ved=2ahUKEwj9po66wIKFAxVsja8BHS0QA9cQ2-cCegQIABAA&oq=%EC%8B%9D%EB%B9%B5&gs_lp=EgNpbWciBuyLneu5tTIIEAAYgAQYsQMyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgARIqT5QmTJY4zxwAXgAkAEAmAHOAaAB0geqAQUwLjcuMbgBA8gBAPgBAYoCC2d3cy13aXotaW1nwgILEAAYgAQYsQMYgwHCAgQQABgDiAYB&sclient=img&ei=Iqn6Zf2NAuyavr0PraCMuA0&bih=909&biw=1718&prmd=isvnmbz")

# 이미지가 로드될 때까지 기다림
wait = WebDriverWait(driver, 50)
wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "img")))

# 페이지의 맨 아래까지 스크롤 다운하여 더 많은 이미지 로드
body = driver.find_element(By.TAG_NAME, "body")
for _ in range(100):  # 스크롤 횟수를 늘리거나 줄일 수 있음
    body.send_keys(Keys.END)
    time.sleep(3)  # 페이지가 로드될 때까지 기다림

# 수정된 이미지 태그를 모두 찾음
images = driver.find_elements(By.TAG_NAME, "img")

# 'dataset' 디렉토리가 없으면 생성
dataset_dir = './dataset/white_bread'  # 여기를 원하는 경로로 수정하세요.
os.makedirs(dataset_dir, exist_ok=True)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.131 Safari/537.36'
}  # User-Agent를 여기에 입력하세요.

for index, image in enumerate(images):
    try:
        src = image.get_attribute('src') or image.get_attribute('data-src')
        if src and '식빵' in image.get_attribute('alt'):
            response = requests.get(src, headers=headers, stream=True)
            if response.status_code == 200:
                with open(os.path.join(dataset_dir, f"white_bread_{index}.jpg"), 'wb') as f:
                    for chunk in response.iter_content(1024):
                        f.write(chunk)
    except Exception as e:
        print(f"An error occurred: {e}")
        continue

driver.quit()
