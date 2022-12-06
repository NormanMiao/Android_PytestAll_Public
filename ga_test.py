# -*- encoding=utf8 -*-
import os
import sys
import time

import wpyscripts.manager as manager
from wpyscripts.common.adb_process import excute_adb_process
print("adb devices: ", flush=True)
os.system("adb devices")
print("adb packages: ", flush=True)
os.system("adb shell pm list package -3")
print("env: ", flush=True)
print(os.environ, flush=True)


app_package = "com.tencent.wetest.demo"
app_activity = "com.unity3d.player.UnityPlayerActivity"


class TestGA:
    engine = None

    @classmethod
    def setup_class(cls):
        excute_adb_process("shell am start -W %s/%s" % (app_package, app_activity))
        time.sleep(5)
        excute_adb_process("shell input keyevent 66")
        excute_adb_process("shell input keyevent 66")
        time.sleep(5)
        cls.engine = manager.get_engine()
        cls.logger = manager.get_logger()

    @classmethod
    def teardown_class(cls):
        excute_adb_process("shell am force-stop %s" % app_package)

    def setup_method(self, method):
        print("setup_method: ", method)
        self.need_return = False

    def teardown_method(self, method):
        print("teardown_method: ", method)
        if self.need_return:
            excute_adb_process("shell input keyevent 4")

    def click_element(self, name, sleep_sec=2):
        find_element_button = self.engine.find_element(name)
        if find_element_button:
            self.engine.click(find_element_button)
            print("click [%s] success" % name)
            time.sleep(sleep_sec)
            return True
        else:
            print("click [%s] failure" % name)
            return False

    def click_elements_path(self, name, sleep_sec=2):
        find_elements_button = self.engine.find_elements_path(name)
        if find_elements_button and len(find_elements_button) > 0:
            self.engine.click(find_elements_button[0])
            print("click [%s] success" % name)
            time.sleep(sleep_sec)
            return True
        else:
            print("click [%s] failure" % name)
            return False

    def test_sample(self):
        self.click_element("/Canvas/Panel/Sample", 3)

    def test_find_elements(self):
        self.need_return = True
        if not self.click_element("/Canvas/Panel/FindElements"):
            print("click find_elements failure, so return")
            return

        self.click_elements_path("/Canvas/Panel/VerticalPanel/Item(Clone)", 2)
        self.click_elements_path("/Canvas/Panel/VerticalPanel/Item(Clone)[1]", 2)
        self.click_elements_path("/Canvas/Panel/VerticalPanel/Item(Clone)[2]", 2)
        self.click_elements_path("/Canvas/Panel/VerticalPanel/Item(Clone)[3]", 2)
        i4 = self.click_elements_path("/Canvas/Panel/VerticalPanel/Item(Clone)[4]", 2)
        assert i4 is not None
        time.sleep(3)
