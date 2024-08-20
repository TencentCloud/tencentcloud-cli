# encoding: utf-8
_lang = "zh-CN"

texts = {
    "zh-CN": {
        "login_prompt": "在浏览器中转到以下链接, 并根据提示完成登录:",
    },
    "en-US": {
        "login_prompt": "Go to the following link in your browser, and complete the sign-in prompts:",
    }
}


def set_lang(lang):
    global _lang
    _lang = lang


def get(key):
    return texts[_lang][key]
