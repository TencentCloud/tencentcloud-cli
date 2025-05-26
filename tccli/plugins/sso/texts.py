# encoding: utf-8
from tccli.plugins.sso import configs

_lang = configs.DEFAULT_LANG

texts = {
    "zh-CN": {
        "invalid_auth_url": "输入的 url 不合法: %s",
        "auth_url_not_configured": "尚未配置 sso url, 使用 `tccli sso configure %s--url https://your-login-domain.com` 来进行配置",
        "configure_succeed": "url 已配置为 '%s', 接下来可以使用 `tccli sso login` 进行登陆",
        "try_login_with_url": "在浏览器中转到以下链接, 并根据提示完成登录:",
        "account_select_prompt": "登录成功, 请选择您的用户: ",
        "role_select_prompt": "请选择您的角色: ",
        "login_success": "登录成功, 密钥凭证已被写入: %s",
        "logout_success": "登出成功, 密钥凭证已被删除: %s",
        "no_account": "未找到成员账号, 请确认是否同步过 CAM 角色",
        "no_role": "当前成员账号不存在授权角色",
        "specified_uin_not_found": "未找到指定的 uin，uin=%s，all=[%s]",
        "specified_role_not_found": "未找到指定的 role, role=%s, all=[%s]",
    },
    "en-US": {
        "invalid_auth_url": "The entered url is invalid: %s",
        "auth_url_not_configured": "sso url is not configured yet, use `tccli sso configure %s--url https://your-login-domain.com` to configure",
        "configure_succeed": "The url has been configured as '%s', use `tccli sso login` to log in",
        "try_login_with_url": "Go to the following link in your browser, and complete the sign-in prompts:",
        "account_select_prompt": "Login succeed, choose your account: ",
        "role_select_prompt": "choose your role: ",
        "login_success": "Login succeed, credential has been written to %s",
        "logout_success": "Logout succeed, credential has been removed: %s",
        "no_account": "no account found, please confirm the account is synchronized",
        "no_role": "no role found in current account",
        "specified_uin_not_found": "Specified uin not found, uin=%s, all=[%s]",
        "specified_role_not_found": "Specified role not found, role=%s, all=[%s]",
    }
}


def set_lang(lang):
    global _lang
    _lang = lang


def get(key):
    return texts[_lang][key]
