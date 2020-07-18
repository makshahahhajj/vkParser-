import time
from selenium.webdriver.common.desired_capabilities import *
from modules import vk_class
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
def parser():
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('log-level=3')  # Set the log level of chromedriver


        driver = webdriver.Chrome( 'C:/chromedriver.exe',chrome_options=chrome_options)

        vk = vk_class.Vk_parser(driver)
        print('Для выхода напишите exit')
        while True:
            print('Type vk-id')
            id = str(input()) 
            if id.strip() == 'exit':
                break
            else:
                vk.load_page(str(id))
                vk.parse_page()

        vk.stop_parser()



   