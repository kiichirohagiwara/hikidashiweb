import time
from selenium import webdriver
import os

word = "test"
path_pycharm = "C:/Users/khagiwara/PycharmProjects/pythonProject1/"
path_image = "word_files/" +word+ "_image.html"
path_sound = "word_files/" +word+ "_sound.html"
path_japanese_meaning = "word_files/" +word+ "_japanese_meaning.html"

def search_image(imported_word):
    driver.get('https://www.google.co.jp/imghp')
    search_box = driver.find_element_by_name("q")
    search_box.send_keys(imported_word)
    search_box.submit()
    time.sleep(5)
    html = driver.page_source
    with open(imported_word +'_image.html', 'w', encoding='utf-8') as f:
        f.write(html)

def search_sound(imported_word):
    driver.get('https://www.oxfordlearnersdictionaries.com/definition/english/'+ imported_word)
    time.sleep(5)
    driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[2]/div[2]/div/div[2]/div/div[1]/div[1]/div/div[1]/div/div/span[2]/div[2]/div').click()
    time.sleep(5)
    html = driver.page_source
    with open(imported_word + '_sound.html', 'w', encoding='utf-8') as f:
        f.write(html)

def search_japanese_meaning(imported_word):
    driver.get('https://ejje.weblio.jp/content/'+imported_word)
    html = driver.page_source
    with open(imported_word + '_japanese_meaning.html', 'w', encoding='utf-8') as f:
        f.write(html)

driver = webdriver.Chrome()
if os.path.exists(path_image):
    driver.get("file:///" + path_pycharm + "word_files/" + word + "_image.html")
    driver.get("file:///" + path_pycharm + "word_files/" + word + "_sound.html")
    driver.get("file:///" + path_pycharm + "word_files/" + word + "_japanese_meaning.html")
    time.sleep(5)
else:
    search_image(word)
    search_sound(word)
    search_japanese_meaning(word)


driver.quit()