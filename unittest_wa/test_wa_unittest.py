# -*- coding: UTF-8 -*-
try:
    from uitrace.api import *
except:
    print("cannot import module uitrace.api")
import unittest

class TestClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """测试类开始执行前执行一次"""
        # 初始化设备驱动和环境
        init_driver(workspace=os.path.dirname(__file__))
        # 返回主页
        press(DeviceButton.HOME)
        
    @classmethod
    def tearDownClass(cls):
        """测试类结束执行后执行一次"""
        stop_driver()

    def setUp(self):
        """测试用例执行前执行一次"""
        # 启动应用：com.tencent.wetestdemo
        start_app("com.tencent.wetestdemo", clear_data=True)
        time.sleep(2)

    def tearDown(self):
        """测试用例执行后执行一次"""
        # 关闭应用：com.tencent.wetestdemo
        stop_app("com.tencent.wetestdemo")

    def test_login_fail(self):
        """不输入账号密码，直接登录——出现Login Failed的弹窗——设置事件处理并启动——弹窗取消"""
        # 查找当前应用，并断言是否为com.tencent.wetestdemo
        app = current_app()
        assert app == "com.tencent.wetestdemo"
        # 点击SIGNIN按钮
        click('//android.view.ViewGroup[@resource-id="com.tencent.wetestdemo:id/container"]/android.widget.Button[@text="SIGNIN" and @resource-id="com.tencent.wetestdemo:id/login"]', by=DriverType.UI, timeout=30)
        # 弹窗Login Failed
        failed_msg = find_ocr(word="Login Failed",timeout=20)
        # ocr文字识别断言内容包含Login Failed的弹窗
        assert failed_msg is not None
        print(failed_msg)
        # 添加事件处理规则-点击OK
        add_event_handler("OK",'OK')
        # 启动事件处理-立即处理
        sync_event_handler()
        # 等待3秒
        time.sleep(3)
        # 再次断言，Login Failed的弹窗已不再出现
        failed_msg = find_ocr(word="Login Failed",timeout=5)
        assert failed_msg is None

    def test_login_success(self):
        """输入账号密码——登录成功——进入SELECT页面——断言左上角SELECT元素存在"""
        # 查找当前应用，并断言是否为com.tencent.wetestdemo
        app = current_app()
        assert app == "com.tencent.wetestdemo"
        # 点击“输入账号”输入框
        click('//android.view.ViewGroup[@resource-id="com.tencent.wetestdemo:id/container"]/android.widget.EditText[@text="Username" and @resource-id="com.tencent.wetestdemo:id/username"]', by=DriverType.UI, timeout=50)
        # 输入账号
        input_text("norman")
        #  点击“输入密码”输入框
        click('//android.view.ViewGroup[@resource-id="com.tencent.wetestdemo:id/container"]/android.widget.EditText[@text="Password" and @resource-id="com.tencent.wetestdemo:id/password"]', by=DriverType.UI, timeout=30)
        # 输入密码
        input_text("123456")
        # 点击登录
        click('//android.view.ViewGroup[@resource-id="com.tencent.wetestdemo:id/container"]/android.widget.Button[@text="SIGNIN" and @resource-id="com.tencent.wetestdemo:id/login"]', by=DriverType.UI, timeout=30)
        # 设置等待2s
        time.sleep(2)
        # 截图
        screenshot(label="screenshot", img_path=None, pos=None)
        # 进入SELECT页面，断言左上角SELECT元素存在
        select = find(loc="//*[@text='SELECT']", by=DriverType.UI, timeout=30)
        assert select is not None


    def test_check_elements(self):
        """登录——勾选item1,item10 """
        # 登录，进入SELECT页
        self.test_login_success()
        # 单击item1
        click(loc="//*[@text='Item1']", by=DriverType.UI, offset=None, timeout=30, duration=0.05, times=1)
        # 双击item3
        double_click(loc="//*[@text='Item3']", by=DriverType.UI, offset=None, timeout=30)
        time.sleep(1)
        # 分别获取item7和item0的坐标，备用        
        pos_from = find(loc="//*[@text='Item7']", by=DriverType.UI, timeout=30)
        pos_to = find(loc="//*[@text='Item0']", by=DriverType.UI, timeout=30)
        # 借助上面获取的坐标滑动屏幕
        slide(loc_from=pos_from, loc_to=pos_to, loc_shift=None, by=DriverType.POS, timeout=30, down_duration=0, up_duration=0, velocity=0.01)
        time.sleep(2)
        # 断言item10存在并获取item10坐标
        item_pos =  find(loc="//*[@text='Item10']", by=DriverType.UI, timeout=30)
        assert item_pos is not None
        # 点击选择item10
        click(loc=item_pos, by=DriverType.POS, offset=None, timeout=30)
        time.sleep(2)
        # 点击提交(CV定位)
        click(loc="obj_1670841033674.jpg", by=DriverType.CV, offset=None, timeout=30, duration=0.05, times=1)
        time.sleep(2)
        # 进入检查页面，检查之前选择的item1和Item10在页面上显示
        select_item =find(loc="obj_1670845223122.jpg", by=DriverType.CV, timeout=30)
        assert select_item is not None
        # 截图
        screenshot(label="screenshot", img_path=None, pos=None)

if __name__ == '__main__':
    unittest.main()
