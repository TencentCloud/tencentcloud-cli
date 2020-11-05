**Example 1: Creating a GME application by using custom configuration**

This example shows you how to use project 10000, enable voice chat with high sound quality, disable voice messaging and speech-to-text, and enable phrase filtering.

Input: 

```
tccli gme CreateApp --cli-unfold-argument  \
    --AppName simple_gme_application\
    --ProjectId 10000,\
    --RealtimeSpeechConf.Status open\
    --RealtimeSpecchConf.Quality high\
    --VoiceMessageConf.Status close\
    --VoiceFilterConf.Status open
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

**Example 2: Creating a GME application by using default configuration**

This example shows you how to create a GME application in the easiest way.

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
            "ProjectId": 0,
            "BizId": 140000001,
            "SecretKey": "abcdefghijklmnop",
            "RealtimeSpeechConf": {
                "Status": "open",
                "quality": "ordinary"
            },
            "VoiceMessageConf": {
                "Status": "close",
                "language": "cnen"
            },
            "VoiceFilterConf": {
                "Status": "close"
            }
        },
        "RequestId": "e2900289-f21e-43a8-a3bf-0b439cdbbbb8"
    }
}
```

