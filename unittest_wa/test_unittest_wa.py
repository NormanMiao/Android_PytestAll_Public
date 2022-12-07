# -*- coding: UTF-8 -*-
try:
    from uitrace.api import *
except:
    print("cannot import module uitrace.api")
import pytest
import unittest

class TestClass(unittest.TestCase):
    @classmethod
    # 初始化类
    def setUpClass(cls):
        init_driver()
        
    @classmethod
    def tearDownClass(cls):
        stop_driver()

    #每个用例开始前初始化
    def setUp(self):
        press(DeviceButton.HOME)
        time.sleep(2)
        start_app("com.tencent.wetestdemo", clear_data=True)
        time.sleep(2)

    def tearDown(self):
        stop_app("com.tencent.wetestdemo")

    def login(self,acc,pwd):
        click('//android.view.ViewGroup[@resource-id="com.tencent.wetestdemo:id/container"]/android.widget.EditText[@text="Username" and @resource-id="com.tencent.wetestdemo:id/username"]', by=DriverType.UI, timeout=50)
        input_text(acc)
        click('//android.view.ViewGroup[@resource-id="com.tencent.wetestdemo:id/container"]/android.widget.EditText[@text="Password" and @resource-id="com.tencent.wetestdemo:id/password"]', by=DriverType.UI, timeout=30)
        input_text(pwd)
        screenshot(label="screenshot", img_path=None, pos=None)
        click('//android.view.ViewGroup[@resource-id="com.tencent.wetestdemo:id/container"]/android.widget.Button[@text="SIGNIN" and @resource-id="com.tencent.wetestdemo:id/login"]', by=DriverType.UI, timeout=30)

    def test_findelement(self):
        self.login("norman","123456")
        # 勾选后进入CHECK页
        click('//android.widget.ListView[@resource-id="com.tencent.wetestdemo:id/list_item"]/android.widget.CheckedTextView[@text="Item0" and @resource-id="android:id/text1"]', by=DriverType.UI, timeout=20)
        click('//android.widget.ListView[@resource-id="com.tencent.wetestdemo:id/list_item"]/android.widget.CheckedTextView[@text="Item3" and @resource-id="android:id/text1"]', by=DriverType.UI, timeout=20)
        screenshot(label="screenshot", img_path=None, pos=None)
        time.sleep(1)
        click('//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.LinearLayout/android.widget.Button[@text="SUBMIT" and @resource-id="com.tencent.wetestdemo:id/submitbtn"]', by=DriverType.UI, timeout=20)
        time.sleep(3)
        find_el = find(loc="obj_1670319758223.jpg", by=DriverType.CV, timeout=30)
        assert(find_el)
        screenshot(label="screenshot", img_path=None, pos=None)

    def test_eventhandle(self):
        self.login("norman","123456")
        """不选择item，直接提交"""
        submit = find(loc="//*[@resource-id='com.tencent.wetestdemo:id/submitbtn']", by=DriverType.UI, timeout=30)
        assert submit is not None
        click(loc=submit, by=DriverType.POS, offset=None, timeout=30, duration=0.05, times=1)
        add_event_handler("(Error|Ok)",'Ok')
        start_event_handler()
        time.sleep(5)


