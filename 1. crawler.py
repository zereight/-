import numpy as np
import pandas as pd
import time
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pickle

# 웹 드라이버를 켠다
# 반드시 파이어 폭스로 실행해주세요.
driver = webdriver.Firefox()
driver.implicitly_wait(1)

keyword = "키워드 입력"
num = 100 #검색할 페이지횟수

# 네이버 블로그 사이트 접속
driver.get(f"https://search.naver.com/search.naver?where=post&sm=tab_jum&query={keyword}")#"https://www.naver.com")
wait = WebDriverWait(driver, 10)

# 이 시간동안 firefox about:config 에 접속해서 javascript:Enabled 를 off 해주세요
time.sleep(20)

# 1~10page까지 수집
blogs = []
for i in range(num):
    time.sleep(1)
    for j in range(1,11):
        try:
            # 글에 썸네일이 있는경우
            blogs.append( driver.find_element_by_css_selector(f'#sp_blog_{j} > div:nth-child(1) > a:nth-child(1)').get_attribute("href") )
        except Exception as e:
            # 글에 썸네일이 없는경우
            blogs.append( driver.find_element_by_css_selector(f'#sp_blog_{j} > dl:nth-child(1) > dt:nth-child(1) > a:nth-child(1)').get_attribute("href") )
    try:
        driver.find_element_by_css_selector("body").send_keys( Keys.COMMAND + Keys.ARROW_DOWN )
        element = driver.find_element_by_css_selector('.next')
        driver.execute_script("arguments[0].click();", element)
    except Exception as e:
        pass



texts = []

for blog_url in blogs:
    try:
        driver.get(blog_url)
        time.sleep(3)
        driver.find_element_by_css_selector("body").click()
        driver.find_element_by_css_selector("body").send_keys(Keys.COMMAND + "a")
        driver.find_element_by_css_selector("body").send_keys(Keys.COMMAND + "c")
        time.sleep(1)
        texts.append( pyperclip.paste() )
        print( pyperclip.paste() )
    except Exception as e:
        continue

with open('data.pickle', 'wb') as f:
    pickle.dump(texts, f, pickle.HIGHEST_PROTOCOL)

    