**Example 1: 查询入侵防御放通封禁列表**

查询入侵防御放通封禁列表

Input: 

```
tccli cfw DescribeBlockIgnoreList --cli-unfold-argument  \
    --Limit 0 \
    --Offset 0 \
    --SearchValue abc \
    --Direction abc \
    --RuleType 1 \
    --Order abc \
    --By abc
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "RuleType": 0,
                "Ioc": "abc",
                "IocInfo": "abc",
                "Domain": "abc",
                "IP": "abc",
                "Level": "abc",
                "EventName": "abc",
                "Direction": 0,
                "DirectionList": "0,1",
                "Protocol": "abc",
                "Address": "abc",
                "Action": 0,
                "StartTime": "abc",
                "EndTime": "abc",
                "IgnoreReason": "abc",
                "Source": "abc",
                "UniqueId": "abc",
                "MatchTimes": 0,
                "Country": "abc",
                "Comment": "abc",
                "LastHitTime": "abc",
                "CustomRule": {
                    "SrcIP": "abc",
                    "DstIP": "abc",
                    "IdsRuleName": "abc",
                    "IdsRuleId": "abc"
                }
            }
        ],
        "Total": 0,
        "ReturnCode": 0,
        "ReturnMsg": "abc",
        "SourceList": [
            "abc"
        ],
        "RuleTypeDataList": [
            0,
            122,
            30,
            55,
            12,
            232,
            0
        ],
        "RequestId": "abc"
    }
}
```

