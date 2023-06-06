**Example 1: 机器人对话服务接口**

文本处理。

Input: 

```
tccli tbp TextProcess --cli-unfold-argument  \
    --BotId 972445 \
    --InputText 北京 \
    --TerminalId 123
```

Output: 
```
{
    "Response": {
        "DialogStatus": "START",
        "BotName": "botname",
        "IntentName": "intentName",
        "SlotInfoList": null,
        "InputText": "hi",
        "ResponseMessage": {
            "GroupList": {
                "ContentType": "text/plain",
                "Url": "www.baidu.com",
                "Content": "hello"
            }
        },
        "ResultType": "1",
        "ResponseText": "xxx",
        "RequestId": "xxx",
        "SessionAttributes": "xxx"
    }
}
```

