# -*- coding:utf8 -*-

from utils import shell, recover_profile


@recover_profile()
def test_auth():
    assert "在浏览器中转到以下链接, 并根据提示完成登录" in shell("tccli auth login --browser no")

    assert "登出成功, 密钥凭证已被删除:" in shell("tccli auth logout")
