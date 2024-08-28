**Example 1: 成功查询**

成功查询

Input: 

```
tccli hunyuan QueryHunyuanImageChatJob --cli-unfold-argument  \
    --JobId test
```

Output: 
```
{
    "Response": {
        "ChatId": "1219898325508988928",
        "History": [
            {
                "ChatId": "1219898325508988928",
                "Prompt": "雪山",
                "RevisedPrompt": "摄影风格，画面主要描述一座雄伟的山峰，山顶覆盖着白雪，阳光照耀下闪耀着光芒，背景是蔚蓝的天空，镜头是全景",
                "Seed": 1763557528
            }
        ],
        "JobErrorCode": "",
        "JobErrorMsg": "",
        "JobStatusCode": "5",
        "JobStatusMsg": "处理完成",
        "RequestId": "da0634c6-7b6b-4115-9081-bd2d20a860ca",
        "ResultDetails": [
            "Success"
        ],
        "ResultImage": [
            "https:/result.jpg"
        ]
    }
}
```

