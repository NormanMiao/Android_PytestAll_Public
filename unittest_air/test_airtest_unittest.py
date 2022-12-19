# -*- encoding=utf8 -*-
try:
    from airtest.core.api import *
    from airtest.cli.parser import cli_setup
    import time
    from poco.drivers.android.uiautomation import AndroidUiautomationPoco
    auto_setup(__file__, logdir=True, devices=["Android:///", ])
    import unittest
except:
    print("cannot import airtest")



class TestWestDemo(unittest.TestCase):
    poco = None

    @classmethod
    def setUpClass(cls):
        cls.poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=True)

    @classmethod
    def tearDownClass(cls):
        cls.poco.stop_running()

    def setUp(self):
        # 清理APP历史数据
        clear_app("com.tencent.wetestdemo")
        time.sleep(0.3)
        start_app("com.tencent.wetestdemo")

    def tearDown(self):
        print("停止app")
        stop_app("com.tencent.wetestdemo")

    def test_login_fail(self):
        """不输入账号密码，直接登录——出现Login Failed的弹窗"""
        # 点击SIGNIN按钮
        self.poco("com.tencent.wetestdemo:id/login").click()
        # 图片识别login failed的弹窗出现
        assert_exists(Template(r"tpl1671115344501.png", record_pos=(-0.207, -0.151), resolution=(1080, 2160)), "登录失败")
        snapshot(msg="登录失败")

    def test_login_success(self):
        """输入账号密码——登录成功——进入SELECT页面——断言左上角SELECT元素存在"""
        # 点击“输入账号”输入框
        self.poco("com.tencent.wetestdemo:id/username").click()
        # 输入账号
        text("norman")
        # 点击“输入密码”输入框
        self.poco("com.tencent.wetestdemo:id/password").click()
        # 输入密码
        text("123456")
        # 点击SIGNIN按钮
        self.poco("com.tencent.wetestdemo:id/login").click()
        sleep(2)
        # 进入SELECT页面，断言左上角Submit元素存在
        submit = self.poco("com.tencent.wetestdemo:id/submitbtn")
        assert submit is not None
        
    def test_check_elements(self):
        """登录——勾选item1,item10 """
        # 登录，进入SELECT页
        self.test_login_success()
        # 单击item1
        self.poco(text="Item1").click()
        # 滑动
        swipe(Template(r"tpl1671116336669.png", record_pos=(-0.061, 0.078), resolution=(1080, 2160)),
              vector=[0.0611, -0.3171])
        # 单击item10
        self.poco(text="Item10").click()
        # 点击提交
        touch(Template(r"tpl1671116431387.png", record_pos=(-0.322, -0.669), resolution=(1080, 2160)))
        # 进入检查页面，检查之前选择的item1和Item10在页面上显示
        check_item = self.poco(text="[Item1, Item10]").exists()
        assert(check_item)

