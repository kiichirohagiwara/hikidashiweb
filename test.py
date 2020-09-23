import time
from selenium import webdriver
import os

path_pycharm = "C:/Users/khagiwara/PycharmProjects/pythonProject1/"


driver = webdriver.Chrome()
driver.get("https://www.oxfordlearnersdictionaries.com/media/english/us_pron/t/tes/test_/test__us_1.mp3")
html = driver.page_source
with open('testsound_japanese_meaning.html', 'w', encoding='utf-8') as f:
    f.write(html)

time.sleep(2)
driver.get("file:///" + path_pycharm + "testsound_japanese_meaning.html")
driver.find_element_by_xpath("//html/body/video/source").click()
time.sleep(3)