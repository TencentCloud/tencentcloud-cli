**Example 1: 成功查询**

成功查询

Input: 

```
tccli hunyuan QueryHunyuanImageChatJob --cli-unfold-argument  \
    --JobId 1253534368-1731657099-7276788a-a326-11ef-beeb-525400bba60c-0
```

Output: 
```
{
    "Response": {
        "ChatId": "1248907282106990592",
        "History": [
            {
                "ChatId": "1248907282106990592",
                "Prompt": "请画一个苹果在桌子上",
                "RevisedPrompt": "风格为摄影风格，桌子上摆放着一个红润的苹果，镜头为近景镜头",
                "Seed": 1549130027
            }
        ],
        "JobErrorCode": "",
        "JobErrorMsg": "",
        "JobStatusCode": "5",
        "JobStatusMsg": "处理完成",
        "RequestId": "54c4d31e-234b-44b8-802b-7d10fa2e77dc",
        "ResultDetails": [
            "Success"
        ],
        "ResultImage": [
            "https://cos.ap-guangzhou.myqcloud.com/***?q-sign-algorithm=sha1&q-ak=xxx&q-sign-time=1731657113;1732261913&q-key-time=1731657113;1732261913&q-header-list=host&q-url-param-list=&q-signature=b9c4be16d763664d829d0bfa398f571aa0e75c0e"
        ]
    }
}
```

