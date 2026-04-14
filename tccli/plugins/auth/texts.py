# encoding: utf-8
_lang = "zh-CN"

texts = {
    "zh-CN": {
        "login_prompt": "您的浏览器已打开, 请根据提示完成登录",
        "login_prompt_no_browser": "在浏览器中转到以下链接, 并根据提示完成登录:",
        "login_prompt_code_no_browser": "完成后，输入浏览器中提供的验证码:",
        "login_failed_due_to_no_browser": "无法打开浏览器, 请尝试添加 '--browser no' 选项",
        "login_success": "登陆成功, 密钥凭证已被写入: %s",
        "logout": "登出成功, 密钥凭证已被删除: %s",
    },
    "en-US": {
        "login_prompt": "Your browser is open, please complete the login according to the prompts",
        "login_prompt_no_browser": "Go to the following link in your browser, and complete the sign-in prompts:",
        "login_prompt_code_no_browser": "Once finished, enter the verification code provided in your browser:",
        "login_failed_due_to_no_browser": "Failed to launch browser, please try option '--browser no'",
        "login_success": "Login succeed, credential has been written to %s",
        "logout": "Logout succeed, credential has been removed: %s",
    }
}


def set_lang(lang):
    global _lang
    _lang = lang


def get(key):
    return texts[_lang][key]
