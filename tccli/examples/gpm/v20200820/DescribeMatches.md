**Example 1: 查询匹配列表**



Input: 

```
tccli gpm DescribeMatches --cli-unfold-argument  \
    --PageNumber 1 \
    --PageSize 10 \
    --SearchType matchCode \
    --Keyword match-58mnuqlz
```

Output: 
```
{
    "Response": {
        "Keyword": "match-58mnuqlz",
        "MatchInfoList": [
            {
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
            }
        ],
        "PageNumber": 1,
        "PageSize": 10,
        "RequestId": "6e0c3a5d-a8cc-4eaf-bdff-214789ac2326",
        "SearchType": "matchCode",
        "TotalCount": 1
    }
}
```

