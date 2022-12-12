# Android_PytestAll_Public
本示例用pytest组织测试用例，完成对qq音乐的测试，包括：使用qq登录qq音乐、使用qq音乐搜索和清除qq音乐缓存。

【用例介绍】
测试用例1: 登录失败场景
不输入账号密码，直接登录，出现Login Failed的弹窗，断言弹窗出现。此时设置事件处理并启动，取消该弹窗并再次断言。
测试用例2: 登录成功场景
输入账号密码，登录成功。进入SELECT页面，查找页面元素并断言。
测试用例3: 检查勾选内容
登录成功后，SELECT页面选中item1和item10，然后进入检查页面，检查之前选择的item1和Item10在页面上显示。

【被测应用及框架】
被测系统：安卓
被测apk:wetestdemo.apk
自动化框架：含wa+appium+ga+airtest，提测时请注意框架与脚本对应。

