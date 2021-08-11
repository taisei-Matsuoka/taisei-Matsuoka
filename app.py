from flask import Flask, render_template
import time
import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import requests
from bs4 import BeautifulSoup
import re
import glob,random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

app = Flask(__name__)  
@app.route('/')
def main():
    return render_template('main.html')
    scraiping()
    
def scraiping():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.youtube.com/channel/UC7F_CLFtxDetmUnORgmwImg')
    searchbtn = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-browse/div[3]/ytd-c4-tabbed-header-renderer/tp-yt-app-header-layout/div/tp-yt-app-header/div[2]/tp-yt-app-toolbar/div/div/tp-yt-paper-tabs/div/div/ytd-expandable-tab-renderer[7]/yt-icon-button/button')
    searchbtn.click()
    time.sleep(5)
    search=driver.find_element_by_css_selector('#input-1 > input').send_keys('腹筋下部')
    searchbtn.send_keys(Keys.ENTER)
    time.sleep(3)
    base=driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer[3]/div[3]/ytd-video-renderer/div[1]/div/div[1]/div/h3/a')
    url=base.get_attribute('href')
    url2= url.replace('https://www.youtube.com/watch?v=','')
    print(url2)
    text = url2
    return render_template('index.html', text=text)

if __name__ == "__main__":
    app.run(debug=True, port=8888, threaded=True)