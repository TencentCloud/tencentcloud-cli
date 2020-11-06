**Example 1: 获取L4转发规则**



Input: 

```
tccli dayu DescribeNewL4Rules --cli-unfold-argument  \
    --Business bgpip \
    --Ip 192.168.1.1 \
    --VirtualPort 123
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "Total": 1,
        "Rules": [
            {
                "Region": 1,
                "Ip": "192.168.1.1",
                "Id": "bgpip-0000011t",
                "RuleId": "rule-000002uq",
                "RuleName": "test",
                "Protocol": "TCP",
                "VirtualPort": 123,
                "SourcePort": 123,
                "SourceType": 2,
                "LbType": 1,
                "KeepTime": 0,
                "ModifyTime": "2020-03-09 21:37:25",
                "SourceList": [
                    {
                        "Source": "119.29.205.248",
                        "Weight": 100
                    }
                ]
            }
        ]
    },
    "Healths": [
        {
            "RuleId": "rule-000002uq",
            "Enable": 0,
            "TimeOut": 6,
            "Interval": 15,
            "KickNum": 5,
            "AliveNum": 5
        }
    ]
}
```

