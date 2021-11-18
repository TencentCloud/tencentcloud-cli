**Example 1: 查询敏感IP信息列表**



Input: 

```
tccli bsca DescribeSensitiveIPList --cli-unfold-argument  \
    --AnalysisId 4a49ab59-cea9-4d19-bed3-326a27465d92 \
    --Limit 2 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "SensitiveIPSet": [
            {
                "IP": "0::CcF",
                "Type": "IPv6",
                "Count": 2,
                "FileList": [
                    {
                        "Name": "/path/demo_text",
                        "Type": "TEXT"
                    },
                    {
                        "Name": "/path/demo_binary",
                        "Type": "BINARY"
                    }
                ]
            },
            {
                "IP": "192.168.1.1",
                "Type": "IPv4",
                "Count": 4,
                "FileList": [
                    {
                        "Name": "/path/demo_text",
                        "Type": "TEXT"
                    },
                    {
                        "Name": "/path/demo_binary",
                        "Type": "BINARY"
                    }
                ]
            }
        ],
        "FieldValuesSet": [
            {
                "Field": "IP",
                "Values": [
                    "ipv4",
                    "ipv6"
                ]
            }
        ],
        "TotalCount": 63,
        "RequestId": "438cb5f7-794c-4073-8b50-dd4ea063517c"
    }
}
```

