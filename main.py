
from modules import vk_class
def init_driver():
        # ua = dict(DesiredCapabilities.CHROME)
        # options = webdriver.ChromeOptions()
        # options.add_argument('headless')
        # options.add_argument('window-size=1920x935')
        # driver  = webdriver.Chrome('C:/chromedriver.exe',chrome_options=options)
        vk = vk_class.Vk_parser()
        vk.init_webdriver()
        vk.laod_page()



        # for li in category:
        #     link_content = li.find_element_by_tag_name('a').get_attribute('textContent')
        #     print(link_content)

        input()



if __name__ == '__main__':
     init_driver()



        

