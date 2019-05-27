import allure
import pytest


class Test03(object):
    @allure.step(title="这事测试03")
    @pytest.allure.severity(pytest.allure.severity_level.MINOR)
    def test03(self):
        with open("./image/自己画的PO流程png.png", "rb") as f:
            allure.attach("截图", f.read(), allure.attach_type.PNG)
        print("test03")
