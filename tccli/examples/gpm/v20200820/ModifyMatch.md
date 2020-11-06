**Example 1: 修改匹配示例**



Input: 

```
tccli gpm ModifyMatch --cli-unfold-argument  \
    --MatchName test \
    --MatchDesc test \
    --RuleCode rule-r4x6tk49 \
    --Timeout 60 \
    --NotifyUrl https://test.com \
    --ServerType 1 \
    --ServerRegion apshanghai \
    --ServerQueue gpmtest \
    --CustomPushData test \
    --ServerSessionData test \
    --LogSwitch 1 \
    --MatchCode match-58mnuqlz \
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
            "CreateTime": "",
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
            "RuleName": "test",
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
        "RequestId": "b6184808-9699-43db-837c-110344620c5d"
    }
}
```

