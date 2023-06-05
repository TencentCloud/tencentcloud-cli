**Example 1: 机器人对话服务接口**

会话重制

Input: 

```
tccli tbp TextReset --cli-unfold-argument  \
    --BotId 972445 \
    --TerminalId 123 \
    --BotEnv dev
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
            "GroupList": [
                {
                    "ContentType": "text/plain",
                    "Url": "www.baidu.com",
                    "Content": "hello"
                },
                {
                    "ContentType": "audio/wav",
                    "Url": "www.baidu.com",
                    "Content": "xccv"
                }
            ]
        },
        "ResultType": "1",
        "ResponseText": "重制会话成功。",
        "RequestId": "xxx",
        "SessionAttributes": "xxx"
    }
}
```

