**Example 1: 使用自定义配置，创建一个GME应用**

使用项目10000，开启实时语音服务，使用高音质；关闭离线语音服务； 开启语音过滤服务

Input: 

```
tccli gme CreateApp --cli-unfold-argument  \
    --AppName simple_gme_application
```

Output: 
```
{
    "Response": {
        "Data": {
            "AppName": "simple_gme_application",
            "CreateTime": 1568945078,
            "ProjectId": 10000,
            "BizId": 140000002,
            "SecretKey": "abcdefghijklmnop",
            "RealtimeSpeechConf": {
                "Status": "open",
                "Quality": "high"
            },
            "VoiceMessageConf": {
                "Status": "open",
                "Language": "cnen"
            },
            "VoiceFilterConf": {
                "Status": "open"
            }
        },
        "RequestId": "d61be8ca-f010-11e9-af81-fa163ee00eb7"
    }
}
```

