**Example 1: 查询蜜罐服务列表**

查询蜜罐服务列表

Input: 

```
tccli cfw DescribeBlockIgnoreList --cli-unfold-argument  \
    --Direction xx \
    --SearchValue xx \
    --RuleType 1 \
    --By xx \
    --Limit 10 \
    --Offset 0 \
    --Order xx
```

Output: 
```
{
    "Response": {
        "ReturnMsg": "xx",
        "ReturnCode": 0,
        "Data": [
            {
                "Domain": "xx",
                "Protocol": "xx",
                "UniqueId": "xx",
                "Level": "xx",
                "Country": "xx",
                "Direction": 0,
                "EventName": "xx",
                "Source": "xx",
                "MatchTimes": 0,
                "StartTime": "xx",
                "Address": "xx",
                "Action": 0,
                "EndTime": "xx",
                "Ioc": "xx",
                "IgnoreReason": "xx"
            }
        ],
        "RequestId": "xx",
        "Total": 1
    }
}
```

