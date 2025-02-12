**Example 1: 使用自定义配置，创建一个GME应用**

创建GME应用123，开启实时语音服务，使用高音质；开启离线语音服务； 关闭语音过滤服务；关闭ASR语音转文本服务。

Input: 

```
tccli gme CreateApp --cli-unfold-argument  \
    --AppName 123 \
    --ProjectId 0 \
    --EngineList android \
    --RegionList mainland \
    --RealtimeSpeechConf.Status open \
    --RealtimeSpeechConf.Quality high \
    --VoiceMessageConf.Status open \
    --VoiceMessageConf.Language all \
    --VoiceFilterConf.Status close \
    --VoiceFilterConf.SceneInfos.0.CallbackUrl http://xxx.xxxrealtimexxx.com \
    --VoiceFilterConf.SceneInfos.0.SceneId RealTime \
    --VoiceFilterConf.SceneInfos.0.Status False \
    --VoiceFilterConf.SceneInfos.1.CallbackUrl http://xxx.xxxvoicemessagexxx.com \
    --VoiceFilterConf.SceneInfos.1.SceneId VoiceMessage \
    --VoiceFilterConf.SceneInfos.1.Status False \
    --VoiceFilterConf.SceneInfos.2.CallbackUrl http://xxx.xxxgmeapixxx.com \
    --VoiceFilterConf.SceneInfos.2.SceneId GMECloudApi \
    --VoiceFilterConf.SceneInfos.2.Status False \
    --AsrConf.Status close \
    --Tags.0.TagKey abc \
    --Tags.0.TagValue abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "AppName": "123",
            "AsrConf": {
                "Status": "close"
            },
            "BizId": 1410000000,
            "CreateTime": 1681894000,
            "ProjectId": 0,
            "RealtimeSpeechConf": {
                "Quality": "high",
                "Status": "open"
            },
            "SecretKey": "7f9xxac16axxx49x",
            "VoiceFilterConf": {
                "SceneInfos": [
                    {
                        "CallbackUrl": "http://xxx.xxxrealtimexxx.com",
                        "SceneId": "RealTime",
                        "Status": false
                    },
                    {
                        "CallbackUrl": "http://xxx.xxxvoicemessagexxx.com",
                        "SceneId": "VoiceMessage",
                        "Status": false
                    },
                    {
                        "CallbackUrl": "http://xxx.xxxgmeapixxx.com",
                        "SceneId": "GMECloudApi",
                        "Status": false
                    }
                ],
                "Status": "close"
            },
            "VoiceMessageConf": {
                "Language": "all",
                "Status": "open"
            }
        },
        "RequestId": "f28xxxfe-8xx8-4xx6-bcxx-22xxxfd00xxx"
    }
}
```

