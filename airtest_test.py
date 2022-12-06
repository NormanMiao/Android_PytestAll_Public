# -*- encoding=utf8 -*-
import os
print(os.environ)
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
auto_setup(__file__)
app_package = "com.oohoo.videocollection"
app_activity = "com.oohoo.videocollection.MainActivity"


class TestVideoCollection:
    poco = None

    @classmethod
    def setup_class(cls):
        cls.poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=True)

    @classmethod
    def teardown_class(cls):
        cls.poco.stop_running()

    def setup_method(self, method):
        print("启动app")
        clear_app(app_package)
        time.sleep(0.3)
        start_app(app_package)
        print("点击进入")
        self.poco("com.oohoo.videocollection:id/welcome_btn").click()

    def teardown_method(self, method):
        print("停止app")
        stop_app(app_package)

    def show_menu(self):
        self.poco("Open navigation drawer").click()
        time.sleep(2)

    def sel_menu_item(self, name):
        self.poco(text="%s" % name).click()
        time.sleep(2)

    def click_first_item(self, timeout=5):
        self.poco("com.oohoo.videocollection:id/video_list")\
            .child("android.widget.LinearLayout")[0].click()
        time.sleep(timeout)

    def test_douban(self):
        self.show_menu()
        self.sel_menu_item("豆瓣Top250")
        self.click_first_item()
        assert_exists(Template(r"tpl1669563928678.png", record_pos=(-0.041, -0.208), resolution=(1080, 2400)), "霸王别姬")

    def test_cloudmusic(self):
        self.show_menu()
        self.sel_menu_item("云音乐")
        self.click_first_item(timeout=20)
        assert_exists(Template(r"tpl1669564411595.png", record_pos=(0.187, 1.056), resolution=(1080, 2400)), "04:27")