**Example 1: 创建匹配示例**



Input: 

```
tccli gpm CreateMatch --cli-unfold-argument  \
    --MatchName test \
    --MatchDesc test \
    --RuleCode rule-r4x6tk49 \
    --Timeout 60 \
    --NotifyUrl https://test.com \
    --ServerType 1 \
    --ServerRegion ap-shanghai \
    --ServerQueue gpmtest \
    --CustomPushData test \
    --ServerSessionData test \
    --LogSwitch 1 \
    --GameProperties.0.Key test \
    --GameProperties.0.Value test \
    --Tags.0.Key 字符串 \
    --Tags.0.Value 字符串
```

Output: 
```
{
    "Response": {
        "MatchInfo": {
            "AppId": "1300704415",
            "CreateTime": "2020-09-29 15:24:19",
            "CreateUin": "100012125188",
            "CustomPushData": "test",
            "GameProperties": [
                {
                    "Key": "test",
                    "Value": "test"
                }
            ],
            "LogSwitch": 1,
            "LogTopicId": "",
            "LogTopicName": "",
            "LogsetId": "",
            "LogsetName": "",
            "MatchCode": "match-58mnuqlz",
            "MatchDesc": "test",
            "MatchName": "test",
            "NotifyUrl": "https://test.com",
            "Region": "ap-shanghai",
            "RuleCode": "rule-r4x6tk49",
            "RuleName": "",
            "ServerQueue": "gpmtest",
            "ServerRegion": "ap-shanghai",
            "ServerSessionData": "test",
            "ServerType": 1,
            "Tags": [
                {
                    "Key": "字符串",
                    "Value": "字符串"
                }
            ],
            "Timeout": 60,
            "Uin": "100012125188"
        },
        "RequestId": "20e5c29d-fa33-45bd-8e90-5b00773fa4cb"
    }
}
```

