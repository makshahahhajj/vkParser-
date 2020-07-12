from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

class Vk_parser(object):
    def __init__(self):
        self.id = ''
    def init_webdriver(self):
        driver = webdriver.Chrome('C:/chromedriver.exe')
        return driver

    def laod_page(self):
        driver = self.init_webdriver()
        driver.get('http://vk.com')
        email_input = driver.find_element_by_id('index_email')
        password_input = driver.find_element_by_id('index_pass')
        login_button = driver.find_element_by_id('index_login_button')
        email_input.send_keys('89166478627')
        password_input.send_keys('maks20043009')
        login_button.click()
        time.sleep(1)
        driver.get('http://vk.com/s_m_i_r_n_o_vv')
        driver.get('https://vk.com/id517514167')

