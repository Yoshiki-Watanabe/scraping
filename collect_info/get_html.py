from selenium import webdriver
from bs4 import BeautifulSoup 
import urllib.request
import sys
import time
import json
import codecs
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class BaseSelenium:

    def __init__(self):
        self.driver = webdriver.Firefox(executable_path="./geckodriver") # 使用ブラウザの設定
        self.user = 'sato_test' # ファイル保存時のフォルダ名
        self.url = "https://www.google.co.jp" # 検索のサイト
        self.keyword = "電子カルテ" # 検索ワード
        self.iter_num = 20 # 何ページ見るか
        self.titles = {} # タイトル保存時のリスト宣言
        self.subword = '株式会社'

    def do_search(self):
        self.driver.get(self.url)

        search_input = self.driver.find_element_by_id("lst-ib")
        search_input.send_keys(self.keyword)

        submit = self.driver.find_element_by_name("btnK")
        submit.click()

    def collect_titles(self):
        self.elements = self.driver.find_elements_by_css_selector("h3.r a")
        self.contents = self.driver.find_elements_by_class_name("st")
        for i, element in enumerate(self.elements):
            if self.subword in element.text:
                if len(self.contents) < i+1:
                    continue
                self.titles.update({element.text:{'contents':self.contents[i].text,'url':element.get_attribute("href")}})
                print(element.text)

    def iterate(self):
        for i in range(self.iter_num - 1):
        # wait = WebDriverWait(self.driver, 10)
        # element = wait.until(EC.presence_of_element_located((By.ID, 'pnnext')))
            nextbtn = self.driver.find_element_by_id("pnnext")
            nextbtn.click()
            self.collect_titles()

    def savejson(self):
        fw = codecs.open('./data/' + self.user+'_list.json', 'w', 'utf-8')
        json.dump(self.titles, fw, indent=4, ensure_ascii=False)


if __name__ == '__main__':

    my_selenium = BaseSelenium()
    my_selenium.do_search()
    my_selenium.collect_titles()
    my_selenium.iterate()
    my_selenium.savejson()







