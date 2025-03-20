**Example 1: 查询系统漏洞列表**



Input: 

```
tccli tcss DescribeSystemVulList --cli-unfold-argument  \
    --Limit 1 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "CVEID": "CVE-2023-3341",
                "CVSSV3Score": 7.5,
                "Category": "OUT_OF_BOUNDS_WRITE",
                "ContainerCount": 0,
                "DefenceHostCount": 0,
                "DefenceScope": "ALL",
                "DefenceStatus": "DEFENDED",
                "DefendedCount": 0,
                "FoundTime": "2024-08-10 04:34:55",
                "ID": 173268083,
                "LatestFoundTime": "2024-10-18 23:30:37",
                "Level": "HIGH",
                "LocalImageCount": 2,
                "Name": "ISC BIND 缓冲区错误漏洞",
                "PocID": "pcmgr-444379",
                "RegistryImageCount": 12,
                "Tags": [
                    "NETWORK"
                ]
            }
        ],
        "RequestId": "5dfca22b-e7b5-408e-b3bf-a930818c5952",
        "TotalCount": 836
    }
}
```

