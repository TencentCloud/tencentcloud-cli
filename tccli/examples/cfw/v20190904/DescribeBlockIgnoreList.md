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
                "Domain": "abc",
                "Ioc": "abc",
                "Level": "abc",
                "EventName": "abc",
                "Direction": 0,
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
                "Comment": "abc"
            }
        ],
        "Total": 0,
        "ReturnCode": 0,
        "ReturnMsg": "abc",
        "SourceList": [
            "abc"
        ],
        "RequestId": "abc"
    }
}
```

