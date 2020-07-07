from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def init_driver():
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get('https://www.wildberries.ru/')
        categories = driver.find_element_by_class_name('topmenus')
        category = categories.find_elements_by_class_name('topmenus-item')

        for li in category:
            link_content = li.find_element_by_tag_name('a').get_attribute('textContent')
            print(link_content)

        input()


if __name__ == '__main__':
     init_driver()