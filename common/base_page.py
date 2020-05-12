import logging
import os
from selenium.webdriver import ActionChains

class BasePage:

    def __init__(self,driver):
        self.driver=driver

    def get_element(self,locator):
        try:
            return self.driver.find_element(*locator)
        except:
            self.driver.save_screenshot(os.path.join,"screenshot2020_05_06")
            logging.error("元素定位失败")

    def drags(self,src,target):
        ac=ActionChains(self.driver)
        ac.drag_and_drop(src,target)
        ac.perform()

    def scroll_to(self,width,height):
        js_code="window.scrollTo({},{})".format(width,height)
        self.driver.execute_script(js_code)