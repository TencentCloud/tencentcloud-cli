**Example 1: 查询匹配示例**



Input: 

```
tccli gpm DescribeMatch --cli-unfold-argument  \
    --MatchCode match-58mnuqlz
```

Output: 
```
{
    "Response": {
        "MatchInfo": {
            "AppId": "1300704415",
            "CreateTime": "2020-09-29 15:24:20",
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
        "RequestId": "ab6ab15a-ab3a-495c-8818-e826084ea072"
    }
}
```

