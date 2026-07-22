# -*- coding:utf8 -*-

from utils import shell, recover_profile


@recover_profile()
def test_sso_configure_and_logout():
    url = "https://tencentcloudsso.com/test/login"
    assert ("url 已配置为 '%s', 接下来可以使用 `tccli sso login` 进行登陆\n" % url ==
            shell("tccli sso configure --url %s" % url))

    assert "登出成功, 密钥凭证已被删除:" in shell("tccli sso logout")
