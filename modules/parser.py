import time
import selenium.webdriver.common.desired_capabilities
from modules import vk_class
def parser():
        # ua = dict(DesiredCapabilities.CHROME)
        # options = webdriver.ChromeOptions()
        # options.add_argument('headless')
        # options.add_argument('window-size=1920x935')
        # driver  = webdriver.Chrome('C:/chromedriver.exe',chrome_options=options)
        vk = vk_class.Vk_parser()
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



   