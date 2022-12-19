# -*- coding: UTF-8 -*-
# coding=utf-8
import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import os
import unittest
app_package ="com.tencent.wetestdemo"
app_activity = "com.tencent.wetestdemo.LoginActivity"

class TestWetestDemo(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        # 定义一个字典，存储capability信息
        desired_caps = {
            "platformName": "Android",
            "appPackage": "com.tencent.wetestdemo",
            "appActivity": "com.tencent.wetestdemo.LoginActivity"
        }
        cls.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)


    @classmethod
    def tearDownClass(cls):
        cls.driver.stop_client()
        print("结束测试")

    def setUp(self):
        print("启动app")
        self.driver.start_activity(app_package, app_activity)
        time.sleep(5)

    def tearDown(self):
        print("停止app")
        self.driver.terminate_app(app_package)


    def test_0_login_fail(self):
        """不输入账号密码，直接登录——出现Login Failed的弹窗"""
        # 判断登录按钮存在
        login = self.driver.find_element(by=AppiumBy.ID,value="com.tencent.wetestdemo:id/login")
        assert login is not None
        # 点击登录
        login.click()
        print("登录失败")
        time.sleep(5)
        # 弹窗出现
        fail_msg = self.driver.find_element(by=AppiumBy.XPATH,
                                            value='//android.widget.Button[@text="OK"]')
        assert fail_msg is not None

    def test_1_login_success_0(self):
        """输入账号密码——登录成功——进入SELECT页面——断言左上角SELECT元素存在"""
        # 输入账号
        acc = self.driver.find_element(by=AppiumBy.ID, value="com.tencent.wetestdemo:id/username")
        acc.click()
        acc.send_keys("norman")
        time.sleep(2)
        # 输入密码
        pwd = self.driver.find_element(by=AppiumBy.ID, value="com.tencent.wetestdemo:id/password")
        pwd.click()
        pwd.send_keys("123456")
        time.sleep(2)
        # 点击登录
        login = self.driver.find_element(by=AppiumBy.ID, value="com.tencent.wetestdemo:id/login")
        login.click()
        time.sleep(5)
        # 进入勾选页，判断submit按钮存在
        submit = self.driver.find_element(by=AppiumBy.ID, value="com.tencent.wetestdemo:id/submitbtn")
        assert submit is not None
        time.sleep(5)


    def test_2_check_elements_1(self):
        """登录——勾选item0,item5，点击提交，进入check页，检查内容为item0和item5"""
        # 登录，进入SELECT页
        self.test_1_login_success_0()
        # 选中item0
        item_0 = self.driver.find_element(by=AppiumBy.XPATH,
                                                value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.'
                                                      'view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.ListView/android.'
                                                      'widget.CheckedTextView[1]')
        item_0.click()
        time.sleep(3)
        # 选中item5
        item_5 = self.driver.find_element(by=AppiumBy.XPATH,
                                          value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.'
                                                'view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.ListView/android.'
                                                'widget.CheckedTextView[6 ]')
        time.sleep(3)
        item_5.click()
        # 点击提交
        self.driver.find_element(by=AppiumBy.ID, value="com.tencent.wetestdemo:id/submitbtn").click()
        time.sleep(5)
        # 进入check页，检查内容为item0和item5（上一页勾选的内容）
        item_check = self.driver.find_element(by=AppiumBy.XPATH,
                                          value='//android.widget.TextView[@text="[Item0, Item5]"]')
        assert item_check is not None
        print("checked")



if __name__ == '__main__':
    unittest.main()
