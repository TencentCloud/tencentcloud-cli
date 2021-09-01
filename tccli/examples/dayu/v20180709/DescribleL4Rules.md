**Example 1: 获取L4转发规则**



Input: 

```
tccli dayu DescribleL4Rules --cli-unfold-argument  \
    --Business bgpip \
    --Id bgpip-000000xe \
    --RuleIdList rule-00000002
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "Total": 1,
        "Rules": [
            {
                "RuleId": "rule-00000002",
                "RuleName": "test",
                "Protocol": "TCP",
                "VirtualPort": 2888,
                "SourcePort": 2888,
                "SourceType": 2,
                "LbType": 1,
                "KeepTime": 300,
                "SourceList": [
                    {
                        "Source": "2.1.1.1",
                        "Weight": 50
                    },
                    {
                        "Source": "2.1.1.2",
                        "Weight": 50
                    }
                ]
            }
        ]
    },
    "Healths": [
        {
            "RuleId": "rule-00000001",
            "Enable": 1,
            "TimeOut": 30,
            "Interval": 300,
            "KickNum": 2,
            "AliveNum": 2
        }
    ]
}
```

