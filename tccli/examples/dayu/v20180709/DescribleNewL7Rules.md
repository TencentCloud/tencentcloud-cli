**Example 1: 获取7层规则**



Input: 

```
tccli dayu DescribleNewL7Rules --cli-unfold-argument  \
    --Business bgpip
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
                "Id": "bgpip-0000011t",
                "Ip": "1.1.1.1",
                "ModifyTime": "2019-12-10 15:15:11",
                "RuleId": "rule-00000002",
                "RuleName": "test",
                "Protocol": "http",
                "VirtualPort": 80,
                "SourcePort": 80,
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
            "Interval": 300,
            "KickNum": 2,
            "AliveNum": 2,
            "Method": "HEAD",
            "StatusCode": 15,
            "Url": "/index.php",
            "Status": 1
        }
    ]
}
```

