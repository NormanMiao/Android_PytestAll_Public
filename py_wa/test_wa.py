# -*- coding: UTF-8 -*-
from uitrace.api import *
import pytest

# test platform start
import os
print("adb devices: ")
print(os.system("adb devices"))
print("env: ")
print(os.environ)
record_dir=os.environ.get("RECORD_DIR")
output_dir = os.path.join(record_dir, "wa_log") if record_dir else ""
# test platform end

class TestVideoCollection:
    @classmethod
    def setup_class(cls):
        init_driver(output_dir=output_dir)
        press(DeviceButton.HOME)
        time.sleep(1)

    @classmethod
    def teardown_class(cls):
        press(DeviceButton.HOME)
        stop_driver()

    def setup_method(self,method):
        start_app("com.oohoo.videocollection",clear_data=True)
        click('//android.widget.RelativeLayout[2]/android.widget.TextView[@text="进入" and @resource-id="com.oohoo.videocollection:id/welcome_btn"]', by=DriverType.UI, timeout=20)
        time.sleep(2)

    def teardown_method(self,method):
        stop_app("com.oohoo.videocollection")
        press(DeviceButton.HOME)
        time.sleep(1)
    
    def test_douban(self):
        click('//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.LinearLayout/android.view.ViewGroup/android.widget.ImageButton', by=DriverType.UI, timeout=20)
        time.sleep(2)
        click('//android.widget.CheckedTextView[@text="豆瓣Top250" and @resource-id="com.oohoo.videocollection:id/design_menu_item_text"]', by=DriverType.UI, timeout=10)
        click('//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[1]', by=DriverType.UI, timeout=10)
        time.sleep(3)
        e1 = find("obj_1670308521845.jpg", by=DriverType.CV, timeout=30)
        assert e1 is not None

    

    def test_cloudmusic(self):
        click('//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.LinearLayout/android.view.ViewGroup/android.widget.ImageButton', by=DriverType.UI, timeout=20)
        time.sleep(2)
        click('//android.widget.CheckedTextView[@text="云音乐" and @resource-id="com.oohoo.videocollection:id/design_menu_item_text"]', by=DriverType.UI, timeout=20)
        click('//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[1]', by=DriverType.UI, timeout=20)
        time.sleep(3)
        e2 = find("obj_1670308935302.jpg", by=DriverType.CV, timeout=30)
        assert e2 is not None
        time.sleep(3)

if __name__ == '__main__':
    pytest.main(['-s',"test_wa.py"])