**Example 1: 创建白盒密钥**



Input: 

```
tccli kms CreateWhiteBoxKey --cli-unfold-argument  \
    --Alias test_alias \
    --Description test_description \
    --Algorithm SM4
```

Output: 
```
{
    "Response": {
        "RequestId": "3691b76c-1ba5-4f93-88ad-858d23ba6c8a",
        "EncryptKey": "AAAAAHP6lsgUa4mYE/cT5LGkquR3xKzUG+cB6oWJ7exbmfR37G6QCB2dEjpdq6+JvmC7cbiDXUFaExxSHQTjlJAzTh/T4p6BZy31uiPXogOnsDEm/vGnh3AJQBopXreiUYe54ZlpJPd/yZocQhsFhiNw2Bmqy6bkp4LrzT2FvzHh5YhwNLRuJnou3G5OecuvaNQoz2L9hkCSc4s7iUaiCMzzDgCnfCYhqgKP+HtaqOMv0LKRzTjSYKxdmzWjPT1vMUxv2Mtk+fF/5gEI6z++eybnWsyJHTx03YnF52sVw5RNs3axXRmOQWUOIoswKmb8M/urWdUio6ZZeE2fMPBg2H2GJvf5wbtCsHLFwdUZBQJ/VcgLXHj0VQxUdUFffL/yZfvIOXAzACvkiZmUEIRP422s5EXIJFfLzA5S+aJgl1Kwp7XI",
        "DecryptKey": "AAAAAHP6lsgUa4mYE/cT5LGkquR3xKzUG+cB6oWJ7exbmfR37G6QCB2dEjpdq6+JvmC7cbiDXUFaExxSHQTjlJAzTh/T4p6BZy31uiPXogOnsDEm/vGnh3AJQBopXreiUYe54ZlpJPd/yZocQhsFhiNw2Bmqy6bkp4LrzT2FvzHh5YhwNLRuJnou3G5OecuvaNQoz2L9hkCSc4s7iUaiCMzzDgCnfCYhqgKP+HtaqOMv0LKRzTjSYKxdmzWjPT1vMUxv2Mtk+fF/5gEI6z++eybnWsyJHTx03YnF52sVw5RNs3axXRmOQWUOIoswKmb8M/urWdUio6ZZeE2fMPBg2H2GJvf5wbtCsHLFwdUZBQJ/VcgLXHj0VQxUdUFffL/yZfvIOXAzACvkiZmUEIRP422s5EXIJFfLzA5S+aJgl1Kwp7XI",
        "KeyId": "3235f222-6e40-11ea-8f2f-5254006d0810",
        "TagMsg": "xx",
        "TagCode": 1
    }
}
```

