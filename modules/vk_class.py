from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys

import time


class Vk_parser(object):
    def __init__(self):
        self.driver = webdriver.Chrome('C:/chromedriver.exe')
        self.driver.get('http://vk.com')
        email_input = self.driver.find_element_by_id('index_email')
        password_input = self.driver.find_element_by_id('index_pass')
        login_button = self.driver.find_element_by_id('index_login_button')
        email_input.send_keys('89166478627')
        password_input.send_keys('maks20043009')
        login_button.click()


    def load_page(self,page_id):
        time.sleep(0.3)
        self.driver.get('http://vk.com/'+ page_id)

    def parse_page(self):
        page_name = self.driver.find_element_by_class_name('page_name')
        print(page_name.text)
    
    def stop_parser(self):
        self.driver.quit()
            