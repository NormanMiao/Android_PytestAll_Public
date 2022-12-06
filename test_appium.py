# -*- coding: UTF-8 -*-
# coding=utf-8
import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# test platform start
import os
print("adb devices: ")
print(os.system("adb devices"))
print("env: ")
print(os.system("env"))
print("appium: ")
print(os.system("ps -ef|grep appium"))

app_package = "com.oohoo.videocollection"
app_activity = "com.oohoo.videocollection.MainActivity"


class TestVideoCollection:
    driver = None

    @classmethod
    def setup_class(cls):
        # 定义一个字典，存储capability信息
        desired_caps = {
            "platformName": "Android",
            "appPackage": app_package,
            "appActivity": app_activity
        }
        cls.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        print("启动测试")

    @classmethod
    def teardown_class(cls):
        cls.driver.stop_client()
        print("结束测试")

    def setup_method(self, method):
        print("启动app")
        self.driver.start_activity(app_package, app_activity)
        print("点击进入")
        welcome_btn = self.driver.find_element(by=AppiumBy.ID, value="welcome_btn")
        welcome_btn.click()

    def teardown_method(self, method):
        print("停止app")
        self.driver.terminate_app(app_package)

    def show_menu(self):
        print("点击显示菜单")
        menu_btn = self.driver.find_element(by=AppiumBy.XPATH,
                                            value='//android.widget.FrameLayout/android.widget.LinearLayout/android'
                                                  '.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                                  '.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android'
                                                  '.view.ViewGroup/android.widget.LinearLayout/android.view.ViewGroup'
                                                  '/android.widget.ImageButton')
        menu_btn.click()
        time.sleep(2)


    def sel_menu_item(self, name):
        print("点击"+name)
        menu_item_btn = self.driver.find_element(by=AppiumBy.XPATH,
                                                 value='//android.widget.CheckedTextView[@text="%s" and '
                                                       '@resource-id="com.oohoo.videocollection:id'
                                                       '/design_menu_item_text"]' % name)
        menu_item_btn.click()
        time.sleep(2)

    def click_first_item(self, timeout=5):
        print("点击第一条")
        item_btn = self.driver.find_element(by=AppiumBy.XPATH,
                                            value='//android.widget.TextView['
                                                  '@resource-id="com.oohoo.videocollection:id/title" and @index="0"]')
        assert item_btn is not None
        item_btn.click()
        time.sleep(timeout)

    def test_douban(self):
        self.show_menu()
        self.sel_menu_item("豆瓣Top250")
        self.click_first_item(timeout=20)

    def test_live(self):
        self.show_menu()
        self.sel_menu_item("直播")
        self.click_first_item(timeout=20)

