from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def init_driver():
    driver = webdriver.Chrome("C:/chromedriver.exe")
    driver.get('https://vk.com')
    input = driver.find_element_by_id('index_email')
    input.send_keys('hello', Keys.ENTER)
    time.sleep(10)
    driver.quit()


if __name__ == '__main__':
     init_driver()
fff