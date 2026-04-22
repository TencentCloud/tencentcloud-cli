**Example 1: 获取批量精准白名单的规则列表**



Input: 

```
tccli waf DescribeBatchCustomWhiteRules --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "ID": 11101,
                "Name": "test",
                "SortId": "100",
                "Strategies": [
                    {
                        "Arg": "",
                        "CompareFunc": "ipmatch",
                        "Content": "1.1.1.2",
                        "Field": "IP"
                    }
                ],
                "Bypass": [
                    "geoip",
                    "cc",
                    "owasp"
                ],
                "JobType": "timed",
                "JobDateTime": {
                    "Timed": [
                        {
                            "StartDateTime": 1711618518,
                            "EndDateTime": 1711918518
                        }
                    ]
                },
                "GroupIds": [
                    1101,
                    1102
                ],
                "ValidStatus": 1,
                "CreateTime": "2020-02-20 14:00:12",
                "Status": "1"
            }
        ],
        "Total": 1,
        "RequestId": "c937ce96-cf53-4df8-b288-07c6e092072d"
    }
}
```

