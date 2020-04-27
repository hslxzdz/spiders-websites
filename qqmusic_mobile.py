from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
import time

class Appaction:
    def __init__(self):
        self.attrs = {
            "platformName": "Android",
            "deviceName": "DUK_AL20",
            "appPackage": "com.tencent.qqmusic",
            "appActivity": "com.tencent.qqmusic.activity.AppStarterActivity",
            "noReset": "True"
        }
        self.server = 'http://localhost:4723/wd/hub'
        self.driver = webdriver.Remote(self.server,self.attrs)
        self.driver.implicitly_wait(5)

    def getUserVideo(self):
        wait = WebDriverWait(self.driver,5,0.5)
        button = self.driver.find_element_by_accessibility_id('我的')
        button.click()
        self.driver.implicitly_wait(2)

        wait = WebDriverWait(self.driver, 5, 0.5)
        button = self.driver.find_element_by_accessibility_id('喜欢')
        button.click()
        self.driver.implicitly_wait(2)

        time.sleep(2)
        vip_list = []
        num = 135
        for item in range(num):
            #定位当前屏幕下每一首歌
            try:
                songs = self.driver.find_elements_by_id('com.tencent.qqmusic:id/aqi')
                for song in songs:
                    try:
                        #定位vip标签
                        vip = song.find_element_by_id('com.tencent.qqmusic:id/dhl')
                    except NoSuchElementException:
                        continue
                    #定位歌名和歌曲信息（包括歌手和专辑）
                    # vip = song.find_element_by_id('com.tencent.qqmusic:id/dhl')
                    name = song.find_element_by_id('com.tencent.qqmusic:id/dhu').get_attribute('text')
                    info = song.find_element_by_id('com.tencent.qqmusic:id/dii').get_attribute('text')
                    print(name, info)
                    # vip_list.append((name, info, vip))
            except NoSuchElementException:
                pass
            self.driver.swipe(start_x=1256, start_y=1931, end_x=1388, end_y=780, duration=1500)
            time.sleep(1)
        return vip_list

if __name__ == '__main__':
    qqmusic = Appaction()
    vip_list = qqmusic.getUserVideo()
    print(vip_list)
